# Requirements Table

## Student Project Portfolio & Showcase App

### Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| **FR-001** | Functional | The system shall enable student teams to create and publish project showcase profiles containing an abstract, demo video link, and verified GitHub repository URL. | High | **Pass:** Profile is published when all required information and a valid repository URL are provided. **Fail:** Profile is published with an invalid repository URL. | Allows student teams to present their projects in a standardized format. |
| **FR-002** | Functional | The system shall enable student teams to upload and manage multimedia project artifacts such as images, presentations, and demonstration videos. | High | **Pass:** Valid multimedia files are successfully uploaded and associated with the project. **Fail:** Unsupported or invalid files are accepted. | Provides judges and visitors with sufficient project information for evaluation. |
| **FR-003** | Functional | The system shall enable panel judges to evaluate submitted projects using predefined digital grading rubrics. | High | **Pass:** Judge can assign scores according to each rubric criterion and submit the evaluation. **Fail:** Evaluation is submitted without required rubric scores. | Ensures consistent and structured project evaluation. |
| **FR-004** | Functional | The system shall enable verified public users to vote for eligible projects while preventing multiple votes from the same user for the same project. | High | **Pass:** A verified user can cast one vote per eligible project. **Fail:** The same user can cast multiple votes for the same project. | Provides fair public participation while reducing fraudulent voting. |
| **FR-005** | Functional | The system shall calculate and display project rankings and leaderboards based on judge scores and public voting results. | Medium | **Pass:** Leaderboard reflects updated scores and votes correctly. **Fail:** Leaderboard displays outdated or incorrectly calculated rankings. | Allows participants and visitors to view project performance and standings. |

### Non-Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| **NFR-001** | Performance & Security | The public voting and leaderboard calculations shall update in real-time with an API response latency below **300 ms** under normal and peak expected load. | High | **Pass:** Benchmarking confirms API response latency remains below 300 ms under simulated peak load. **Fail:** Response latency exceeds 300 ms. | Ensures responsive voting and leaderboard functionality. |
| **NFR-002** | Security | The system shall implement authentication and anti-sybil mechanisms to ensure that only verified users can vote and that fraudulent or duplicate voting attempts are prevented. | High | **Pass:** Duplicate and unverified voting attempts are rejected during security testing. **Fail:** An unverified user or duplicate account can successfully cast additional votes. | Protects the fairness and integrity of the public voting system. |
