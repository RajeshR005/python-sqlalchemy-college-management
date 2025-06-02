# 🎓 College Database Management System – SQLAlchemy Based (In Progress)

![College DB Banner](https://raw.githubusercontent.com/RajeshR005/python-sqlalchemy-college-management/main/assets/college_banner.gif)

A fully functional **College Database Management System** built using **Python and SQLAlchemy ORM**.  
This project is a real-world application created as part of my internship, and it goes beyond basic student record management to implement **role-based access**, **department-wise control**, and **data integrity validations** — all tailored to manage students, staff, and admin functionalities.

---

## 📘 Project Overview

This system simulates a real-world college ERP where each user role is restricted and empowered to manage only their scope of data:

- 👨‍🎓 **Students**
  - Can log in and update only their own personal information.
  - No access to other student data or academic records.

- 👨‍🏫 **Staff**
  - Can manage their own profile.
  - Can **view, add, and update students** only in **their own department**.

- 🧑‍💼 **Admin**
  - Has full control over the system.
  - Can create/update/delete:
    - Departments
    - Students
    - Staff
    - Courses and Assignments
    - Course enrollments for students and staff

---

## 🧱 Features

- ✅ **Role-Based Access Control (RBAC)**
- ✅ **Department-wise Isolation**
- ✅ **Course Enrollment Handling**
- ✅ **Student-Staff-Course Linkage via Relationships**
- ✅ **ORM-Based Models with SQLAlchemy 1.4+**
- ✅ **Scalable Architecture with Clean Design**
- 🔐 **Secure Update Operations for Each Role**
- 🛠️ **Future Plans:** Integration with FastAPI for UI, Authentication, and Web API

---

## ⚙️ Technologies Used

- 🔹 **Python 3.9+**
- 🔹 **SQLAlchemy ORM 1.4+**
- 🔹 **MySQL** 
- 🔹 **Virtualenv** for isolation

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/RajeshR005/python-sqlalchemy-college-management.git
cd python-sqlalchemy-college-management
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

```bash
python database/db_setup.py
python database/seed_data.py
```

### 5. Run Sample Role Operations

```bash
python crud/student_crud.py
python crud/staff_crud.py
python crud/admin_crud.py
```

---

## 🎯 Learning Objectives

- Understand SQLAlchemy ORM for advanced use-cases
- Build and manage complex relationships between tables
- Apply RBAC in a database system
- Practice clean modular Python architecture
- Prepare for full-stack development by building backend logic

---

## 🔒 Access Permissions Overview

| Role    | Can Read Own Data | Can Edit Own Data | Can Access Others | Assign Courses | Manage System |
|---------|-------------------|-------------------|-------------------|----------------|----------------|
| Student | ✅                | ✅                | ❌               | ❌             | ❌             |
| Staff   | ✅                | ✅                | ✅ (same dept)   | ❌             | ❌             |
| Admin   | ✅                | ✅                | ✅               | ✅             | ✅             |

---

## 📸 Visuals & ER Diagrams

![ER Diagram](https://raw.githubusercontent.com/RajeshR005/python-sqlalchemy-college-management/main/assets/er_diagram.gif)

---

## 👨‍💻 Author

**Rajesh R – Python Developer Intern**  
📧 [rajeshr005@gmail.com](mailto:rajeshr005@gmail.com)  
🔗 [GitHub](https://github.com/RajeshR005) | [Portfolio](https://rajeshr005.github.io/Healthcare-website/)  

[![Gmail](https://img.shields.io/badge/Gmail-rajeshr005%40gmail.com-red?logo=gmail&logoColor=white)](mailto:rajeshr005@gmail.com)

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

> 🚧 **Project is under active development — more automation, validations using FastAPI and a frontend are coming soon.**
