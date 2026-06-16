# Digital Nurture 5.0 — DotNet FSE Deep Skilling (Angular Track)



## What is this program?

This is Cognizant's Deep Skilling program that builds on the Upskilling foundation. Over 7 weeks, you'll go from core engineering concepts all the way to deploying containerized microservices, building frontend applications with Angular, and working with GenAI tools.

Before diving in — make sure you've completed the Upskilling handbook first. OOP fundamentals are the backbone of everything covered here.

---

## Skills at a Glance

| Construct | Skills |
| --- | --- |
| Engineering Concepts | Design Patterns & Principles, Data Structures & Algorithms

 |
| Programming Languages | Advanced SQL (SQL Server), NUnit & Moq

 |
| Products & Frameworks | Entity Framework Core 8, ASP.NET Core Web API, Microservices, Angular

 |
| Platforms | Git, CI/CD, Docker

 |
| Emerging Tech | Gen AI Fundamentals

 |

---

## Timeline

```
Week 1        → Design Patterns + DSA (Engineering Concepts)
Week 2        → Advanced SQL + NUnit & Moq
Weeks 3–4    → Entity Framework Core 8
Weeks 4–5    → ASP.NET Core Web API
Week 5.5     → Microservices Architecture
Weeks 6–7    → Angular + Debugging + Git + Docker + DevOps + Agile + GenAI

```

**Time commitment:** 10–12 hours/week. Spread across daily 1–2 hour sessions or longer weekend blocks.

---

## How Learning Works

**Two components run in parallel:**

1. **Self-paced learning** — open-source reference links provided for each module


2. **Bi-weekly SME sessions** — live expert sessions (100% attendance mandatory)



To complete the program, you must finish all hands-on exercises AND pass the final Knowledge-Based Assessment (KBA).

---

## Tools to Install

| Tool | Link |
| --- | --- |
| Visual Studio Community | [Download](https://visualstudio.microsoft.com/vs/community/)<br> |
| SQL Server Management Studio | [Download](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)<br> |
| VS Code | [Download](https://code.visualstudio.com/download)<br> |

---

## Getting the Exercises

All hands-on exercises are in the public GitHub repo. Here's the workflow:

1. Go to the repo → click **Code → Download ZIP**

2. Check the file `DN - DotNet FSE Mandatory hands-on detail.xlsx` for which exercises are mandatory vs optional


3. Solve each problem, organize solutions week-wise in a folder


4. Upload to your own public GitHub repo and share the URL when asked



---

## Modules

### Module 1 — Design Patterns & Principles *(~2 days)*

Covers SOLID principles (SRP, OCP, LSP, ISP, DIP) and the most common Gang of Four patterns — Singleton, Factory, Builder, Adapter, Decorator, Proxy, Observer, Strategy, and Command. Also touches on MVC and Dependency Injection as architectural patterns.

| Topic | Reference |
| --- | --- |
| SOLID Principles | [Baeldung Guide](https://www.baeldung.com/solid-principles)<br> |
| Design Patterns (GoF + Architectural) | [Medium Article](https://medium.com/@softwaretechsolution/design-pattern-81ef65829de2)<br> |

✅ Design Patterns Quiz · 🛠️ Hands-on exercises

---

### Module 2 — Data Structures & Algorithms *(~2 days)*

Focus is on time/space complexity analysis and implementing the most common data structures and algorithms from scratch.

| Topic | Reference |
| --- | --- |
| Algorithm Analysis (Big O, Best/Avg/Worst) | [GFG DSA](https://www.geeksforgeeks.org/design-and-analysis-of-algorithms/)<br> |
| Sorting (Bubble, Insertion, Heap, Quick, Merge) | [GFG Sorting](https://www.geeksforgeeks.org/sorting-algorithms/)<br> |
| Arrays | [GFG Arrays](https://www.geeksforgeeks.org/array-data-structure-guide/)<br> |
| Linked Lists (Single, Double, Circular) | [GFG Linked List in C#](https://www.google.com/search?q=https://www.geeksforgeeks.org/linked-list-in-DotNet/)<br> |
| Searching (Linear, Binary) | [GFG Searching](https://www.google.com/search?q=https://www.geeksforgeeks.org/searching-algorithms/%23basics-of-searching-algorithms)<br> |

✅ DSA Quiz · 🛠️ Hands-on exercises

---

### Module 3 — Advanced SQL (SQL Server) *(~2 days)*

Goes beyond basic queries into window functions, stored procedures, transactions, and error handling — things you'll use constantly in enterprise .NET work.

| Topic | Key Sub-topics |
| --- | --- |
| Advanced Concepts | Window functions (OVER, PARTITION BY, RANK, DENSE_RANK), CTEs, MERGE, PIVOT, UNPIVOT

 |
| Views & Indexes | Creating/modifying views, index types, covering indexes, query optimization

 |
| Stored Procedures & Functions | Create/execute/modify SPs, scalar & table-valued functions

 |
| Triggers & Cursors | DML triggers (AFTER, INSTEAD OF), cursor lifecycle, cursor alternatives

 |
| Exception Handling | TRY/CATCH, THROW, RAISERROR

 |
| Transactions | ACID properties, savepoints, isolation levels, deadlocks

 |

🛠️ Hands-on exercises

---

### Module 4 — NUnit & Moq *(~1 day)*

Unit testing in .NET. This module teaches you to write clean, trustworthy tests and mock out dependencies so you can test components in isolation.

| Topic | Key Sub-topics |
| --- | --- |
| Getting Started | Test pyramid, TDD, NUnit setup in Visual Studio

 |
| Unit Testing Fundamentals | Naming tests, parameterized tests, setup/teardown, what to test

 |
| Core Techniques | Testing strings, arrays, void methods, exception-throwing methods, code coverage

 |
| Mocking with Moq | Dependency injection patterns, creating mock objects, state vs. interaction testing

 |

**References:** [NUnit Intro](https://www.google.com/search?q=https://www.csharpcorner.com/article/introduction-to-nunit-testingframework-/) · [Moq Guide](https://www.codemag.com/Article/2305041/Using-Moq-A-Simple-Guide-to-Mocking-for-.NET)

🛠️ Hands-on exercises

---

### Module 5 — Entity Framework Core 8.0 *(~1 week)*

ORM in .NET using EF Core 8. You'll define data models, run migrations, and interact with SQL Server using LINQ — no raw SQL needed.

| Topic | Key Sub-topics |
| --- | --- |
| EF Core Overview | ORM concept, EF Core vs EF Framework, new EF Core 8 features

 |
| Setup | NuGet packages, DbContext config, CLI commands (add migration, update database)

 |
| Data Modeling | Entities, relationships, primary/foreign keys, code-first approach

 |
| CRUD Operations | AddAsync, Find, FirstOrDefault, ToListAsync, Remove, DeleteRange

 |
| LINQ Queries | Where, Select, OrderBy, DTOs, async queries

 |
| Migrations | Add/remove/update migrations, seed data

 |
| Relationships & Loading | Eager, lazy, explicit loading; one-to-one, one-to-many, many-to-many

 |
| Performance | AsNoTracking, bulk operations, RowVersion concurrency, compiled queries

 |

**Reference:** [DotNet Tutorials EF Core](https://dotnettutorials.net/lesson/entity-framework-core/)

🛠️ Hands-on exercises

---

### Module 6 — ASP.NET Core 8.0 Web API *(~1.5 weeks)*

Building RESTful APIs from the ground up. Covers the full lifecycle — project setup, controllers, routing, auth, error handling, logging, and documentation.

| Topic | Key Sub-topics |
| --- | --- |
| Introduction | REST vs SOAP, .NET 8 project structure

 |
| Building APIs | Controllers, actions, routes, CRUD with EF Core, JSON serialization

 |
| Advanced Features | Attribute routing, middleware, filters, JWT authentication & role-based authorization

 |
| SOAP Services | WCF overview, consuming and creating SOAP services

 |
| Security & Error Handling | Global exception handling, CORS, Serilog logging, API key / OAuth

 |
| Documentation & Testing | Swagger/OpenAPI integration, Postman, REST Client

 |

**Reference:** [DotNet Tutorials Web API series](https://dotnettutorials.net/lesson/introduction-to-asp-net-core-web-api/)

🛠️ Hands-on exercises

---

### Module 7 — Microservices Architecture *(~0.5 week)*

Conceptual and practical introduction to breaking monoliths into microservices using ASP.NET Core Web API.

| Topic | Key Sub-topics |
| --- | --- |
| Architecture Overview | Microservices vs monolith, advantages and challenges

 |
| Communication & Data | HTTP/messaging/gRPC, service discovery, database-per-service pattern

 |
| Security & Monitoring | JWT auth, health checks, logging strategies

 |
| Deployment | Rolling updates, blue-green deployments, CI/CD with GitHub Actions / Azure DevOps, Docker & Kubernetes basics

 |

**Reference:** [GFG Inter-service Communication](https://www.geeksforgeeks.org/inter-service-communication-in-microservices/)

🛠️ Hands-on exercises

---

### Module 8 — Angular (v20.0) *(~2 weeks)*

Builds dynamic web applications with Angular. Covers framework architecture up to API integrations and state management.

| Topic | Key Sub-topics |
| --- | --- |
| Introduction & Setup | Angular framework overview, project setup via Angular CLI, running and building applications

 |
| Components | Component creation, interaction via Data Binding (Property, Event, Two-way), lifecycle hooks, @Input and @Output

 |
| Directives & Pipes | Built-in structural (*ngIf, *ngFor, *ngSwitch) and attribute directives, custom directives, built-in and custom pipes

 |
| Forms | Template-driven forms, Reactive forms with FormBuilder, FormControl, FormGroup, FormArray, built-in and custom validators

 |
| Services & DI | Dependency Injection concepts, creating and using Angular Services, hierarchical injection levels

 |
| Routing & Navigation | Configuring routes, route/ query parameters, nested routes, lazy loading modules, router guards, passing data

 |
| HTTP Client & APIs | Setting up HttpClientModule, making GET/POST/PUT/DELETE requests, handling responses with Observables, HTTP Interceptors

 |
| State Management | State management problems, using services for state, NgRx (Store, Actions, Reducers, Effects, Selectors)

 |
| Reactive Programming | RxJS Observables, common operators (map, filter, switchMap, mergeMap, catchError), reactive patterns

 |
| Testing Angular | Unit testing with Jasmine and Karma, component and service testing, E2E testing overview

 |

**Skill Spring Course:** .NET Backend Engineer (includes frontend modules)

✅ [Angular Quiz 1](https://www.javaguides.net/2023/09/angular-quiz.html) · [Angular Quiz 2](https://www.w3schools.com/angular/angular_quiz.asp) · 🛠️ Hands-on (use VS Code)

---

### Module 9 — Application Debugging *(Angular focus)*

Practical debugging skills using Chrome DevTools and VS Code for Angular/TypeScript applications.

| Tool | What you'll learn |
| --- | --- |
| Chrome DevTools | DOM tree inspection, Sources panel, breakpoints, call stack, TypeScript source maps

 |
| VS Code Debugger | Extension setup, launch.json configuration, setting breakpoints and watches, debugging state management (NgRx)

 |

✅ [Debugging Quiz](https://www.geeksforgeeks.org/quizzes/error-handling-and-debugging/) · [Chrome DevTools Quiz](https://wayground.com/admin/quiz/66f797ec1ff0b846272b8a4e/mastering-chrome-dev-tools)

---

### Module 10 — Version Control with Git *(part of Week 7)*

Everything from initializing a repo to collaborating via pull requests and managing branching workflows.

| Topic | Key Sub-topics |
| --- | --- |
| Concepts | VCS types, distributed vs centralized

 |
| Git Basics | init, clone, add, commit, status, log

 |
| Branching & Merging | Create/switch branches, merge conflicts, Git Flow

 |
| Remote Repos | push, pull, tracking remote branches

 |
| Collaboration | Fork, pull requests, Gitflow workflow

 |

**Reference:** [GFG Git Tutorial](https://www.geeksforgeeks.org/git-tutorial/)

🛠️ Hands-on exercises

---

### Module 11 — DevOps & CI/CD *(part of Week 7)*

Awareness-level module on how modern dev teams ship software continuously.

| Topic | Key Sub-topics |
| --- | --- |
| DevOps | Goals, benefits, key practices

 |
| CI/CD | What CI vs CD means, benefits, difference between them

 |
| Tools | Jenkins, GitHub Actions, GitLab CI/CD, CircleCI

 |

**Reference:** [GFG DevOps Tutorial](https://www.geeksforgeeks.org/devops-tutorial/)

✅ DevOps Quiz

---

### Module 12 — Containerization with Docker *(part of Week 7)*

How to package and run applications in containers — and an intro to orchestration with Kubernetes.

| Topic | Key Sub-topics |
| --- | --- |
| Docker Commands | run, ps, stop, rm, images, pull, exec

 |
| Docker Run | Named containers, detached mode, port publishing

 |
| Docker Images | Image layers, Dockerfile method, build context

 |
| Docker Compose | YAML config, multi-container setups

 |
| Storage & Networking | Volumes, data persistence, default and custom networks

 |
| Orchestration | What Kubernetes solves, container orchestration vs Docker Swarm

 |

**Reference:** [GFG Docker Tutorial](https://www.geeksforgeeks.org/docker-tutorial/)

✅ Docker Quiz

---

### Module 13 — Agile Methodology *(part of Week 7)*

How real software teams plan and deliver work using Agile/Scrum.

| Topic | Key Sub-topics |
| --- | --- |
| Agile Manifesto | 4 values, 12 principles, Agile vs Waterfall

 |
| Scrum | Scrum Master / Product Owner / Dev Team roles, Sprint ceremonies, artifacts

 |
| Estimation | Story points, planning poker, velocity, burndown charts

 |
| User Stories | Format: "As a [user], I want [goal]…", INVEST principle, Given-When-Then criteria

 |

**Skill Spring Course:** ITPM - Introduction to Agile [101-Basics]

---

### Module 14 — Gen AI Fundamentals *(part of Week 7)*

Introduction to Generative AI and hands-on use of GitHub Copilot as a coding assistant.

| Topic | Key Sub-topics |
| --- | --- |
| What is GenAI | How it differs from traditional AI, history (chatbots → GANs → GPT → Copilot)

 |
| Prompt Engineering | Zero-shot, few-shot, chain-of-thought prompting, best practices, ethical use

 |
| GitHub Copilot | Setup in VS Code, generating code from comments, writing tests, refactoring

 |
| Risks & Responsibility | AI hallucinations, licensing/attribution, data privacy, responsible use

 |

**Skill Spring Courses:** Prompt Engineering Foundation [101-BASIC] · GitHub Copilot Foundation

✅ [GenAI Quiz](https://www.mygreatlearning.com/blog/generative-ai-quiz/) · [Copilot Practice Test](https://examsland.com/free-practice-test/github-copilot/)

---

## Completion Checklist

* [ ] Finish all mandatory hands-on exercises (check the `.xlsx` file in the repo)


* [ ] Attend all bi-weekly SME connect sessions


* [ ] Complete module quizzes as you go


* [ ] Pass the final Knowledge-Based Assessment (KBA)