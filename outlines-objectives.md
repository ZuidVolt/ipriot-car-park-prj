
# Objectives

By completing this task, you will demonstrate the following competencies as outlined in **ICTPRG430**:

- **Modularity:** Implement the program using a modular approach.
- **Data Structures:** Utilize arrays of primitive data types within a class.
- **File Operations:** Read from and write to a text file.
- **Class Design:** Develop multiple classes in response to a specification.
- **Object Aggregation:** Employ user-defined object aggregation within a class.
- **Polymorphism:** Implement polymorphism to enhance code extensibility.
- **Debugging:** Use a debugging tool to troubleshoot your code.
- **Code and Documentation Conventions:** Apply specified coding and documentation standards.
- **Unit Testing:** Conduct and document unit tests.

As part of this assessment, you will also demonstrate competencies in using a version control system, as outlined in **ICTICT449**. You will plan, install, create, and manage a repository to control versions of your code for the system you implement to complete the scenario. You must follow the commit and branching standards outlined in the NMS onboarding guide.

---

# Scenario

The City of Moondalup is progressively embracing smart city initiatives to enhance urban living, improve efficiency in city services, and promote sustainable practices. As part of this initiative, the city council is eager to transition to a smart parking solution to optimize carpark usage, reduce traffic congestion, and enhance the overall parking experience for residents and visitors.

You have been contracted to create a prototype solution that uses sensors and displays to provide timely information about available parking bays as well as relevant information about weather and other community messages.

The city’s Chief Technology Officer (CTO) has outlined the following requirements:

- The system must accurately track and show availability of bays in real-time.
- The displays must be able to show ambient temperature and arbitrary announcements.
- The system must store the scanned license plates of cars.
- The system must work in uncontrolled car parks.
- The display must be updated promptly as cars enter or exit.
- The system should be robust, easy to maintain, and scalable for future enhancements.
- The application must follow best coding practices and include unit tests.
- You must use Git and GitHub for version management.

---

# Coding Requirements

To meet the specifications of the project, you must do the following:

- Create at least **three classes**.
- At least **one class** must include **three or more parameters**.
- At least **one class** must aggregate another class.
- At least **one class** must include a **list (array) of primitive data types**.
- Demonstrate an example of **polymorphism**.
- Include at least **two unit tests**.
- **Read and write configuration from a file**.
- Allow carpark to be constructed either from a direct call or via the configuration file (**two options for object construction**).
- Create a `main.py` demonstrating the core interaction between instances of your classes.
- Use **PEP8** throughout your code and **docstrings** for major functions within your code.
- Record and provide evidence of **debugging**.
- Apply at least **three different documentation conventions** (README, docstring, comments).

---

# Version Control Requirements

- Follow the guidelines in the **NMS Onboarding guide**.
- Create a new repository and configure it with a `README`, `.gitignore`, and other essential setup files.
- Initialize your local repository and link it to a remote repository on GitHub.
- Create a branch with your work.
- Make initial commits with the basic structure of your Carpark system.
- As you develop the system, commit your changes each time you reach a significant milestone or complete a task.
- Make at least **three commits** to demonstrate the evolution of your project (please note, if you use the project guide to develop your project, you will be asked to make additional commits as proof-of-work).
- Ensure that any downtime or service interruptions that may result from your changes are clearly communicated.
- Manage any changes or improvements by committing to the repository with clear, descriptive commit messages.
- Finalize your submission by documenting the final outcome by:
    1. Pushing your changes to your branch
    2. Creating a descriptive PR
    3. Merging the PR with `main`
    4. Pulling from the remote `main` to the local `main`
    5. Deleting the branch both locally and remotely
    6. Adding an annotated tag and pushing to git
    7. Adding release documentation
