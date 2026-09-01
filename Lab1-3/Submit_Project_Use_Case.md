# Use-Case Flow Specification

## UC-01: Submit Project

**Primary Actor:** Student Team

### Preconditions

1. The student team is registered and authenticated.
2. The student team has created a project profile.
3. Required project information has been entered.
4. The project contains the required multimedia artifacts and repository information.

### Postconditions

**Success:**
- The project is successfully submitted.
- The project is validated.
- The project becomes available in the showcase catalog for eligible judges and public users.

**Failure:**
- The project remains unpublished.
- The student team is informed about the validation error.

### Main Success Scenario

1. Student Team logs into the showcase application.
2. Student Team selects **Create/Manage Project**.
3. Student Team enters the project title and abstract.
4. Student Team adds the demo video link.
5. Student Team provides the GitHub repository URL.
6. Student Team uploads the required project artifacts.
7. Student Team selects **Submit Project**.
8. System validates the project information.
9. System verifies that the GitHub repository URL is valid.
10. System confirms successful validation.
11. System publishes the project to the showcase catalog.
12. System displays a confirmation message to the Student Team.

### Alternate Flow

#### A1 — Invalid GitHub Repository URL

1. During validation, the system detects that the GitHub repository URL is invalid or inaccessible.
2. The system rejects the submission.
3. The system displays an error message requesting a valid repository URL.
4. Student Team corrects the URL.
5. Student Team resubmits the project.
6. System performs validation again.
