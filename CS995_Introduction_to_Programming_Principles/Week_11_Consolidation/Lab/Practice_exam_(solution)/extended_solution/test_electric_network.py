import unittest
from electric_network import State, UnitType, Element


class TestState(unittest.TestCase):
    def test_repr(self):
        state = State(1234, "a name")
        new_state = eval(str(state))
        self.assertEqual(state.id, new_state.id)
        self.assertEqual(state.name, new_state.name)


class TestUnitType(unittest.TestCase):
    def test_repr(self):
        unit_type = UnitType(1234, "a name", 2.0)
        new_unit_type = eval(str(unit_type))
        self.assertEqual(unit_type.id, new_unit_type.id)
        self.assertEqual(unit_type.name, new_unit_type.name)
        self.assertEqual(unit_type.current, new_unit_type.current)


class TestElement(unittest.TestCase):
    def test_repr(self):
        state = State(1234, "a name")
        unit_type = UnitType(1234, "a name", 2.0)
        child_element = Element(2, unit_type, state, [])
        element = Element(1, unit_type, state, [child_element])
        new_element = eval(str(element))
        self.assertEqual(element.id, new_element.id)
        self.assertEqual(element.unit_type.id, new_element.unit_type.id)
        self.assertEqual(element.state.id, new_element.state.id)
        self.assertEqual(len(element.child_elements),
                         len(new_element.child_elements))

    def test_total_current(self):
        state_on = State(1, "On")
        bulb = UnitType(1, "Bulb", 0.05)
        branch = UnitType(2, "Branch", 0)
        branch_element = Element(1, branch, state_on, [
            Element(2, bulb, state_on, []),
            Element(3, bulb, state_on, [])
        ])
        self.assertAlmostEqual(2*bulb.current, branch_element.total_current())

    def test_find_max_load(self):
        state_on = State(1, "On")
        bulb = UnitType(1, "Bulb", 0.05)
        big_load = UnitType(1, "Big load", 10)
        branch = UnitType(2, "Branch", 0)
        branch_element = Element(1, branch, state_on, [
            Element(2, bulb, state_on, []),
            Element(3, big_load, state_on, [])
        ])
        max_element = branch_element.find_max_load()
        self.assertAlmostEqual(3, max_element.id)


if __name__ == "__main__":
    unittest.main()
