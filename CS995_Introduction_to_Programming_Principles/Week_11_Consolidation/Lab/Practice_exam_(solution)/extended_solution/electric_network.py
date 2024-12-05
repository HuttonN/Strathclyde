import json
import os


class State:
    """
    A class to represent a network element state
    within an electrical network.
    """
    def __init__(self,
                 id=0,
                 name=""):
        self.id = id
        self.name = name

    def __repr__(self):
        s = "State("
        s += f"id={self.id},"
        s += f"name=\"{self.name}\""
        s += ")"
        return s


class UnitType:
    """
    A class to represent a network element type
    within an electrical network.
    """
    def __init__(self,
                 id=0,
                 name="",
                 current=0.):
        self.id = id
        self.name = name
        self.current = current

    def __repr__(self):
        s = "UnitType("
        s += f"id={self.id},"
        s += f"name=\"{self.name}\","
        s += f"current={self.current}"
        s += ")"
        return s


class Element:
    """
    A class to represent a network element within
    an electrical network.
    """
    def __init__(self,
                 id=0,
                 unit_type=None,
                 state=None,
                 child_elements=[]):
        self.id = id
        self.unit_type = unit_type
        self.state = state
        self.child_elements = child_elements.copy()

    def __repr__(self):
        s = "Element("
        s += f"id={self.id},"
        s += f"unit_type={self.unit_type},"
        s += f"state={self.state},"
        s += f"child_elements={self.child_elements},"
        s += ")"
        return s

    def total_current(self):
        """
        A function to return the total current that is
        associated with this network element.
        """

        # If the network element is not on.
        if self.state.name != "On":
            return 0

        # If the network element has not child elements.
        if len(self.child_elements) == 0:
            return self.unit_type.current

        # Calculate the current by summing the child elements.
        current_sum = 0
        for element in self.child_elements:
            current_sum += element.total_current()
        return current_sum

    def find_max_load(self):
        """
        A function to return the element that draws the
        biggest current that is connected to this element.
        """

        # No child elements.  Therefore, no maximum load.
        if len(self.child_elements) == 0:
            return None

        # Loop over child elements to find maximum load.
        max_current = -1
        max_element = None
        for element in self.child_elements:
            element_current = element.total_current()
            if element_current > max_current:
                max_current = element_current
                max_element = element
        return max_element


def check_keys(json_data, keys):
    """
    A function to verify a JSON dictionary.
    """
    if not isinstance(json_data, dict):
        return False
    for key in keys:
        if key not in json_data.keys():
            return False
    return True


def load_states(json_data, states):
    """
    A function to load states, creating objects
    as needed.
    """
    states.clear()
    if not isinstance(json_data, list):
        return False
    for json_obj in json_data:
        if not check_keys(json_obj, [
            "id",
            "name"
        ]):
            return False
        id = int(json_obj["id"])
        if id not in states:
            states[id] = State(id, str(json_obj["name"]))
    return True


def load_types(json_data, unit_types):
    """
    A function to load unit types, creating objects
    as needed.
    """
    unit_types.clear()
    if not isinstance(json_data, list):
        return False
    for json_obj in json_data:
        if not check_keys(json_obj, [
            "id",
            "name",
            "current"
        ]):
            return False
        id = int(json_obj["id"])
        if id not in unit_types:
            unit_types[id] = UnitType(id,
                                      str(json_obj["name"]),
                                      float(json_obj["current"]))
    return True


def load_elements(json_data,
                  states,
                  unit_types,
                  elements):
    """
    A function to load elements, creating objects
    as needed.
    """
    elements.clear()
    for json_obj in json_data:
        if not check_keys(json_obj, [
            "id",
            "type_id",
            "state_id",
            "element_ids"
        ]):
            return None

        element_id = int(json_obj["id"])
        type_id = int(json_obj["type_id"])
        state_id = int(json_obj["state_id"])

        if type_id not in unit_types.keys():
            msg = f"Cannot find type_id:{type_id} "
            msg += f"for element id:{element_id}."
            print(msg)
            return False
        if state_id not in states.keys():
            msg = f"Cannot find state_id:{state_id} "
            msg += f"for element id:{element_id}."
            print(msg)
            return False

        elements[element_id] = Element(element_id,
                                       unit_types[type_id],
                                       states[state_id])
    return True


def find_child_elements(json_data,
                        elements):
    """
    A function to find child elements.
    """
    for json_obj in json_data:

        # Consider elements with child elements.
        child_ids = json_obj["element_ids"]
        if len(child_ids) == 0:
            continue

        element_id = int(json_obj["id"])

        # In case the elements have not been loaded first.
        if element_id not in elements.keys():
            print("Error: the elements have not been loaded.")
            return False

        # Append the child element.
        element = elements[element_id]
        for child_id in child_ids:
            if child_id not in elements.keys():
                print("Error: the child element has not been loaded.")
                False
            element.child_elements.append(elements[child_id])
    return True


def load_network(file_name, elements):
    """
    A function to load the electrical network,
    creating objects as needed.
    """
    if not os.path.isfile(file_name):
        return False
    input_file = open(file_name, "r", encoding="utf8")
    json_data = json.load(input_file)
    input_file.close()
    if not check_keys(json_data, [
        "elements",
        "states",
        "unit_types"
    ]):
        return False
    states = {}
    if not load_states(json_data["states"], states):
        return False
    unit_types = {}
    if not load_types(json_data["unit_types"], unit_types):
        return False
    elements.clear()
    if not load_elements(json_data["elements"],
                         states,
                         unit_types,
                         elements):
        return False
    if not find_child_elements(json_data["elements"],
                               elements):
        return False
    return True


def main():
    """
    A program to load the network elements and associated
    objects, printing the electric current and maximum
    load information.
    """

    # Load the configuration of the electrical network.
    elements = {}
    file_name = "electric_network.json"
    if not load_network(file_name,  elements):
        return
    print(f"Loaded data from {file_name}.")

    # Find the maximum loads and print associated information.
    for element in elements.values():
        max_load_element = element.find_max_load()
        msg = f"{element.unit_type.name} (id:{element.id}) "
        msg += f"total current: {element.total_current()}A"
        if max_load_element is not None:
            msg += f", max load: {max_load_element.unit_type.name}"
            msg += f" (id:{max_load_element.id})."
        else:
            msg += "."
        print(msg)


if __name__ == "__main__":
    main()
