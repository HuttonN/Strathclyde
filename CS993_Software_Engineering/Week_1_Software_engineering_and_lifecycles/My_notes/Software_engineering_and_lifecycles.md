# Software Engineering and Lifecycles (TO FINISH!!!)

## Software Engineering

### Historical Perspective: Apollo Guidance Computer
- **Apollo 11 Lunar Module** was a milestone in software engineering.
- Key constraints:
  - **Limited computational power** & memory.
  - **Safety-critical system** (failure could lead to astronaut fatalities).
  - **Structured development approach** was necessary.
- Led to the emergence of structured **software engineering practices**.

---

### Software Development Scenarios
- Various software delivery configurations:
  1. **Internal development team** for company projects.
  2. **Development team with external customers**.
  3. **Product owner inside the customer's company**.
  4. **Middle management layer between development & customer** (often problematic).

- **Challenges**:
  - Need to **understand and satisfy stakeholders**.
  - **Frequent releases** for maintainability.
  - **Communication issues** between development and business teams.

---

## Teams and Risks
- Typical roles in a **development team**:
  - **Lead Developer**
  - **Project Manager**
  - **Test Engineers**
  - **Developers**
  - **Release/Deployment Managers**

- **Risks in software projects**:
  - Knowledge loss if a **lone developer** leaves.
  - **Lack of documentation** leads to maintenance issues.
  - Poor **interface design** causing integration problems.
  - **Bad issue tracking** delays defect resolution.

---

## Development Approaches
- **Prototyping: Developer-Led**
  - Understanding **hardware & software frameworks**.
  - **Testing algorithms** before full-scale development.
  - **Performance testing** to predict deployment needs.

- **Prototyping: User-Led**
  - Building **UI/UX prototypes** to gather feedback.
  - **Implicit commitment** to users’ expectations.
  - Incremental **enhancements based on user feedback**.

- **Bottom-Up Approach**:
  - Start with **hardware constraints**.
  - Build low-level **drivers & interfaces**.

- **Top-Down Approach**:
  - Start with **user requirements**.
  - Define the **user interface & workflows**.
  - Implement backend **logic & functionality**.

---

## Development Lifecycles

## Software Development Life Cycle
### Standard Steps:
1. **Requirement Definition** – Capturing what the customer wants.
2. **System Design** – High-level architecture.
3. **Implementation & Unit Testing** – Developing and testing components.
4. **Integration & System Testing** – Assembling the software.
5. **Operation & Maintenance** – Deploying & maintaining the system.

- **Traceability**: Ensuring features are:
  - **Defined** (who requested it, why it's needed).
  - **Validated** (how it was tested).
  - **Documented** (release version, known issues).

---

## Software Development Models
### 1. **Waterfall Model**
- **Linear and structured** process:
  - Requirements → Design → Implementation → Verification → Deployment.
- **Pros**:
  - Well-defined **cost & schedule** estimation.
- **Cons**:
  - **Rigid process**, difficult to adapt to changes.
  - **Long development cycles**, may lead to **outdated** requirements at delivery.

### 2. **V-Model (Verification & Validation)**
- A variation of Waterfall with **validation steps at each phase**.
- Used in **safety-critical** industries (nuclear, military).
- **Less flexible**, mostly used for **initial builds**.

### 3. **Spiral Model**
- **Iterative approach**, incorporating risk management.
- Prototyping → Requirements Refinement → Design → Development → Testing.
- Suitable for **large-scale** projects with evolving requirements.

### 4. **Rapid Application Development (RAD)**
- Focuses on **fast prototyping** and iterative refinement.
- Useful for projects where **user feedback is essential**.

---

## Agile Lifecycles

### Agile Software Manifesto
- **Individuals & Interactions** over processes and tools.
- **Working Software** over comprehensive documentation.
- **Customer Collaboration** over contract negotiation.
- **Responding to Change** over following a plan.

### Agile Principles:
- **Continuous delivery** to keep customers satisfied.
- **Late modifications are acceptable** if needed.
- **Small, working iterations** are delivered frequently.
- **Encourage communication** between developers and owners.

### Waterfall vs Agile:
| Aspect         | Waterfall       | Agile         |
|---------------|----------------|--------------|
| Requirements  | Fixed upfront   | Evolve over time |
| Cost & Schedule | Estimated initially | Adaptable |
| Stakeholder Involvement | Minimal | Continuous |
| Risk         | High (late discovery) | Lower (frequent iterations) |

### Agile Scrum
- **Product backlog**: List of features.
- **Sprint backlog**: Selected tasks for a development cycle (2-4 weeks).
- **Daily Scrum**: 10-15 min stand-up meetings.
- **Sprint review**: Demonstrating completed features.
- **Sprint retrospective**: Discussing improvements for the next cycle.

- **Common Agile Practices**:
  - **Daily stand-ups** for team communication.
  - **Sprint planning & retrospectives** for iterative improvements.
  - **Test-driven development (TDD)** to maintain code quality.

---

## Development Failures

### Causes of Software Failures:
1. **Incorrect Requirements Capture** – Software isn’t what the client wanted.
2. **Compatibility Issues** – Software fails on customer infrastructure.
3. **Defects & Bugs** – Issues only appear after deployment.
4. **Bad Issue Tracking** – Defects reappear due to poor documentation.
5. **No Clear Definition of Completion** – Software keeps evolving without formal delivery.

### Case Study: Police Scotland i6 Project Failure
- **Errors in technical coding & system design**.
- **Contractor underestimated complexity**.
- **Disputes over project scope** → **£24.65M loss**.
- **Lack of compliance** with security & data standards.

---

## Conclusion
- **Software Engineering is critical** for successful projects.
- **Different development models** exist (Waterfall, Agile, Spiral, etc.).
- **Agile is the most widely used** approach today (especially Scrum).
- **Failure to manage development properly** can be **very costly**.
- **Early failure detection is key** ("Fail Fast" methodology).
- **Continuous delivery** ensures client satisfaction.

---

These notes summarize the key concepts from the lecture, combining **practical examples**, **historical context**, and **modern software development practices**.