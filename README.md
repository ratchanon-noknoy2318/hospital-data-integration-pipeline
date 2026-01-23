### Patients table

| HOSxP Field (`person` table)   | `patients` Table Field | Type         | Description                     |
| :---                           | :---                   | :---         | :---                            |
| `p.cid`                        | `citizen_id`           | VARCHAR(13)  | National ID (UNIQUE, NOT NULL)  |
| `p.pname` (from `pname` table) | `title`                | VARCHAR(20)  | Title (e.g., นาย, นาง, นางสาว)  |
| `p.fname`                      | `first_name`           | VARCHAR(100) | First Name                      |
| `p.lname`                      | `last_name`            | VARCHAR(100) | Last Name                       |
| `p.birthdate`                  | `birthdate`            | DATE         | Full Date of Birth              |
| `p.sex`                        | `gender`               | TINYINT      | Gender (1=Male, 2=Female)       |
| `h.address` (parsed)           | `house_number`         | VARCHAR(50)  | House Number                    |
| `h.road`                       | `road`                 | VARCHAR(100) | Road Name                       |
| `v.village_name`               | `village_name`         | VARCHAR(100) | Village Name                    |

---

**Contact and Profiles**
* **LinkedIn:** [linkedin.com/in/ratchanon-noknoy/](https://www.linkedin.com/in/ratchanon-noknoy/)
* **GitLab:** [ratchanon.noknoy2318](https://gitlab.com/ratchanon.noknoy2318)
