# Pillar 1 — System Design

Status: Canonical component specification v1.0  
Research provenance: recovered Builders Academy pillar research; authoritative source register refreshed 31 August 2026.  
Component count: 30

Each entry is retrieval-ready and may be used to generate study notes, slides, coach notes, labs, assignments, co-tutor prompts, assessments, project applications and governance assets. The “Recovered research synthesis” preserves the non-generic source context; the structured fields make it operational.

## P1-C01 — Requirements and System Boundaries

**Classification:** Must Know

**Core Principle:** Start with what the product actually does, who uses it, critical user journeys, functional requirements, non-functional requirements, constraints, dependencies, regulatory requirements, geographic requirements and what is explicitly outside the system.

**Why It Matters:** Students should distinguish business requirements from technical solutions. Microsoft explicitly recommends beginning architecture from business needs and balancing functional and non-functional requirements.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about requirements and system boundaries, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Start with what the product actually does, who uses it, critical user journeys, functional requirements, non-functional requirements, constraints, dependencies, regulatory requirements, geographic requirements and what is explicitly outs…
- Students should distinguish business requirements from technical solutions.
- Microsoft explicitly recommends beginning architecture from business needs and balancing functional and non-functional requirements.

**Practical Mental Model:** Treat Requirements and System Boundaries as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- Student must answer: Who uses my system?
- What must it do?
- Which journeys cannot fail?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add requirements and system boundaries” without requirements, constraints, acceptance evidence or review triggers.
- Which journeys cannot fail?

**AI-Building Implications:** Make the Requirements and System Boundaries decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Requirements and System Boundaries to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a requirements and system boundaries decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P2-C01 Simplicity; P2-C03 Modularity; P2-C18 Secure-by-Design Software; P2-C19 Testing as a Design Practice

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02)

<details><summary>Recovered research synthesis</summary>

Start with what the product actually does, who uses it, critical user journeys, functional requirements, non-functional requirements, constraints, dependencies, regulatory requirements, geographic requirements and what is explicitly outside the system. Students should distinguish business requirements from technical solutions. Microsoft explicitly recommends beginning architecture from business needs and balancing functional and non-functional requirements. 

   **Student must answer:** Who uses my system? What must it do? Which journeys cannot fail? What external systems does it depend on? What does success look like?

</details>

---

## P1-C02 — Capacity Estimation and Workload Understanding

**Classification:** Must Know

**Core Principle:** Before discussing scaling, students need the ability to estimate users, concurrent users, requests per second, read/write ratio, peak traffic, file uploads, average object size, bandwidth, database growth, storage growth and expected future growth.

**Why It Matters:** Google SRE specifically recommends using actual capacity testing rather than assumptions and warns that launch traffic can differ sharply from steady-state load. A vibe coder does not need advanced capacity mathematics.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about capacity estimation and workload understanding, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Before discussing scaling, students need the ability to estimate users, concurrent users, requests per second, read/write ratio, peak traffic, file uploads, average object size, bandwidth, database growth, storage growth and expected fut…
- Google SRE specifically recommends using actual capacity testing rather than assumptions and warns that launch traffic can differ sharply from steady-state load.
- A vibe coder does not need advanced capacity mathematics.

**Practical Mental Model:** Treat Capacity Estimation and Workload Understanding as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes capacity estimation and workload understanding necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Headroom and responsiveness versus infrastructure cost, complexity and premature optimisation.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add capacity estimation and workload understanding” without requirements, constraints, acceptance evidence or review triggers.
- A vibe coder does not need advanced capacity mathematics.

**AI-Building Implications:** Make the Capacity Estimation and Workload Understanding decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Capacity Estimation and Workload Understanding to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a capacity estimation and workload understanding decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P5-C21 Server vs Serverless; P6-C01 Testing Mindset; P6-C13 Load Testing; P6-C14 Stress Testing

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04)

<details><summary>Recovered research synthesis</summary>

Before discussing scaling, students need the ability to estimate users, concurrent users, requests per second, read/write ratio, peak traffic, file uploads, average object size, bandwidth, database growth, storage growth and expected future growth. Google SRE specifically recommends using actual capacity testing rather than assumptions and warns that launch traffic can differ sharply from steady-state load. 

   A vibe coder does **not** need advanced capacity mathematics. They do need to stop saying: *"It should handle plenty of users."*

   They should instead be able to say: *"We expect approximately 10,000 registered users, 1,000 daily active users, 100 peak concurrent users and approximately X GB of new storage per month."*

</details>

---

## P1-C03 — High-Level Architecture

**Classification:** Must Know

**Core Principle:** Students should understand client, frontend, backend, database, storage, external services and infrastructure boundaries.

**Why It Matters:** They need monolith vs modular monolith vs microservices conceptually, serverless vs long-running services, synchronous vs asynchronous workflows, stateful vs stateless services, and managed vs self-managed infrastructure. A crucial Builders Academy principle should be: Start with the simplest architecture that satisfies today's requirements while preserving a path to evolve.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about high-level architecture, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Students should understand client, frontend, backend, database, storage, external services and infrastructure boundaries.
- They need monolith vs modular monolith vs microservices conceptually, serverless vs long-running services, synchronous vs asynchronous workflows, stateful vs stateless services, and managed vs self-managed infrastructure.
- A crucial Builders Academy principle should be: Start with the simplest architecture that satisfies today's requirements while preserving a path to evolve.

**Practical Mental Model:** Treat High-Level Architecture as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes high-level architecture necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add high-level architecture” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the High-Level Architecture decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply High-Level Architecture to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a high-level architecture decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** See the pillar index and adjacent production lifecycle components.

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02)

<details><summary>Recovered research synthesis</summary>

Students should understand client, frontend, backend, database, storage, external services and infrastructure boundaries. They need monolith vs modular monolith vs microservices conceptually, serverless vs long-running services, synchronous vs asynchronous workflows, stateful vs stateless services, and managed vs self-managed infrastructure.

   A crucial Builders Academy principle should be:

   **Start with the simplest architecture that satisfies today's requirements while preserving a path to evolve.**

   Microsoft specifically warns against unnecessary complexity and recommends designing for evolution through loose coupling and well-defined interfaces.

</details>

---

## P1-C04 — Data Architecture

**Classification:** Must Know

**Core Principle:** This deserves much more attention than most vibe-coding courses give it.

**Why It Matters:** Students should understand entities, relationships, schemas, normalisation at a practical level, SQL vs NoSQL, transactional vs analytical data, structured vs unstructured data, database constraints, data ownership, source of truth, indexes, query patterns, migrations, connection limits, retention and deletion. Then gradually introduce replication, partitioning, sharding, read replicas and distributed data when the product actually requires them.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about data architecture, then failing under real load, change or dependency loss.

**Concepts to Master:**

- This deserves much more attention than most vibe-coding courses give it.
- Students should understand entities, relationships, schemas, normalisation at a practical level, SQL vs NoSQL, transactional vs analytical data, structured vs unstructured data, database constraints, data ownership, source of truth, inde…
- Then gradually introduce replication, partitioning, sharding, read replicas and distributed data when the product actually requires them.

**Practical Mental Model:** Treat Data Architecture as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- Student must answer: What data exists?
- Where does it live?
- How is it related?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add data architecture” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Data Architecture decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Data Architecture to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a data architecture decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P6-C28 Data Protection; P1-C12 Concurrency, Consistency and Data Integrity; P3-C52 Analytics & Behaviour Data; P5-C37 Data Transformation

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02)

<details><summary>Recovered research synthesis</summary>

This deserves much more attention than most vibe-coding courses give it. Students should understand entities, relationships, schemas, normalisation at a practical level, SQL vs NoSQL, transactional vs analytical data, structured vs unstructured data, database constraints, data ownership, source of truth, indexes, query patterns, migrations, connection limits, retention and deletion.

   Then gradually introduce **replication, partitioning, sharding, read replicas and distributed data** when the product actually requires them. Microsoft explicitly identifies partitioning as a way of overcoming database, network and compute limits, while warning that partition-key design must avoid hotspots. 

   **Student must answer:** What data exists? Where does it live? How is it related? What grows fastest? What is sensitive? What gets deleted? What queries will happen most frequently?

</details>

---

## P1-C05 — Storage Architecture

**Classification:** Must Know

**Core Principle:** Students need to distinguish database storage from object/blob storage, cache, local filesystem and archival storage.

**Why It Matters:** Images, videos, PDFs and large uploads should not automatically be thrown into database rows. They should calculate approximate storage needs and think about upload limits, file types, retention, backups, access control, lifecycle management and delivery.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about storage architecture, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Students need to distinguish database storage from object/blob storage, cache, local filesystem and archival storage.
- Images, videos, PDFs and large uploads should not automatically be thrown into database rows.
- They should calculate approximate storage needs and think about upload limits, file types, retention, backups, access control, lifecycle management and delivery.

**Practical Mental Model:** Treat Storage Architecture as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes storage architecture necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** More relevant information versus token cost, privacy exposure, stale context and retrieval noise.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add storage architecture” without requirements, constraints, acceptance evidence or review triggers.
- Images, videos, PDFs and large uploads should not automatically be thrown into database rows.

**AI-Building Implications:** Make the Storage Architecture decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Storage Architecture to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a storage architecture decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P5-C19 Object Storage; P4-C35 Model Selection; P5-C13 Tokens & JWTs; P5-C18 Database as Infrastructure

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02)

<details><summary>Recovered research synthesis</summary>

Students need to distinguish database storage from object/blob storage, cache, local filesystem and archival storage. Images, videos, PDFs and large uploads should not automatically be thrown into database rows.

   They should calculate approximate storage needs and think about upload limits, file types, retention, backups, access control, lifecycle management and delivery.

</details>

---

## P1-C06 — API and Communication Design

**Classification:** Must Know

**Core Principle:** This is where frontend, backend and third-party systems meet.

**Why It Matters:** Students should understand REST conceptually, endpoints, requests/responses, HTTP methods, status codes, authentication, versioning, pagination, validation, API contracts, SDKs, webhooks, GraphQL conceptually and realtime communication such as WebSockets/SSE where appropriate. They should understand synchronous communication vs asynchronous communication and why tightly coordinating every component can limit scalability.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about api and communication design, then failing under real load, change or dependency loss.

**Concepts to Master:**

- This is where frontend, backend and third-party systems meet.
- Students should understand REST conceptually, endpoints, requests/responses, HTTP methods, status codes, authentication, versioning, pagination, validation, API contracts, SDKs, webhooks, GraphQL conceptually and realtime communication s…
- They should understand synchronous communication vs asynchronous communication and why tightly coordinating every component can limit scalability.

**Practical Mental Model:** Treat API and Communication Design as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes api and communication design necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add api and communication design” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the API and Communication Design decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply API and Communication Design to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a api and communication design decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P4-C14 API vs MCP; P5-C02 API Fundamentals; P5-C05 API Contracts; P5-C06 API Documentation

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04), [API-01](source-register.md#api-01)

<details><summary>Recovered research synthesis</summary>

This is where frontend, backend and third-party systems meet. Students should understand REST conceptually, endpoints, requests/responses, HTTP methods, status codes, authentication, versioning, pagination, validation, API contracts, SDKs, webhooks, GraphQL conceptually and realtime communication such as WebSockets/SSE where appropriate.

   They should understand **synchronous communication vs asynchronous communication** and why tightly coordinating every component can limit scalability. Microsoft explicitly recommends minimising coordination and using asynchronous communication where appropriate.

</details>

---

## P1-C07 — Performance and Latency

**Classification:** Must Know

**Core Principle:** "Fast" must become measurable.

**Why It Matters:** Students should understand latency, throughput, response time, network latency, database latency, frontend performance, backend performance, bottlenecks and P50/P95/P99 at a practical level. Google SRE demonstrates SLOs using latency distributions rather than averages because different portions of users experience different response times.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about performance and latency, then failing under real load, change or dependency loss.

**Concepts to Master:**

- "Fast" must become measurable.
- Students should understand latency, throughput, response time, network latency, database latency, frontend performance, backend performance, bottlenecks and P50/P95/P99 at a practical level.
- Google SRE demonstrates SLOs using latency distributions rather than averages because different portions of users experience different response times.

**Practical Mental Model:** Treat Performance and Latency as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes performance and latency necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Headroom and responsiveness versus infrastructure cost, complexity and premature optimisation.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add performance and latency” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Performance and Latency decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Performance and Latency to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a performance and latency decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P6-C12 Performance Testing; P7-C16 Production AI: Reliability, Latency & Cost; P3-C35 Perceived Performance; P6-C45 Metrics

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04), [API-05](source-register.md#api-05)

<details><summary>Recovered research synthesis</summary>

"Fast" must become measurable. Students should understand latency, throughput, response time, network latency, database latency, frontend performance, backend performance, bottlenecks and P50/P95/P99 at a practical level.

   Google SRE demonstrates SLOs using latency distributions rather than averages because different portions of users experience different response times. 

   Builders Academy should repeatedly ask:

   **Where is the time being spent?**

   Browser → network → API → authentication → application → database → external dependency → response.

</details>

---

## P1-C08 — Caching and Content Delivery

**Classification:** Must Know

**Core Principle:** Students should understand browser caching, CDN caching, application caching and database/query caching, plus cache hit/miss, TTL, invalidation, stale data and cache stampedes.

**Why It Matters:** Redis's current cache-aside guidance illustrates the central trade-off nicely: longer TTLs improve hit rates and reduce primary-database load, but increase the window in which stale data can be served. This becomes a beautiful Builders Academy question: What data in your application can safely be slightly old?

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about caching and content delivery, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Students should understand browser caching, CDN caching, application caching and database/query caching, plus cache hit/miss, TTL, invalidation, stale data and cache stampedes.
- Redis's current cache-aside guidance illustrates the central trade-off nicely: longer TTLs improve hit rates and reduce primary-database load, but increase the window in which stale data can be served.
- This becomes a beautiful Builders Academy question: What data in your application can safely be slightly old?

**Practical Mental Model:** A cache is a fast temporary copy with an explicit staleness budget, not a new source of truth.

**Student Decision Questions:**

- Which measured read or delivery bottleneck justifies caching?
- How stale may this data safely become for this user journey?
- What event or TTL invalidates it, and who owns that rule?
- Can key design expose another user or tenant's data?
- What happens on a cold cache, stampede or cache outage?

**Trade-offs:** Lower latency, bandwidth and origin load versus stale data, invalidation complexity, memory cost and new failure modes such as hot keys and stampedes.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add caching and content delivery” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Caching and Content Delivery decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Caching and Content Delivery to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a caching and content delivery decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P3-C33 Content Priority; P3-C05 Layout & Composition; P3-C42 Familiarity & Mental Models; P5-C15 Webhooks

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02)

<details><summary>Recovered research synthesis</summary>

Students should understand browser caching, CDN caching, application caching and database/query caching, plus cache hit/miss, TTL, invalidation, stale data and cache stampedes.

   Redis's current cache-aside guidance illustrates the central trade-off nicely: longer TTLs improve hit rates and reduce primary-database load, but increase the window in which stale data can be served. 

   This becomes a beautiful Builders Academy question:

   **What data in your application can safely be slightly old?**

</details>

---

## P1-C09 — Scalability

**Classification:** Must Know

**Core Principle:** Students need vertical scaling, horizontal scaling, elasticity, stateless services, autoscaling, bottleneck identification and understanding that different parts of the application may scale differently.

**Why It Matters:** They should also understand that scaling is not simply "add more servers." Instances may disappear during scale-in, long-running jobs may need checkpoints, and work may need queues so another worker can continue processing. Microsoft specifically highlights those behaviours.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about scalability, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Students need vertical scaling, horizontal scaling, elasticity, stateless services, autoscaling, bottleneck identification and understanding that different parts of the application may scale differently.
- They should also understand that scaling is not simply "add more servers." Instances may disappear during scale-in, long-running jobs may need checkpoints, and work may need queues so another worker can continue processing.
- Microsoft specifically highlights those behaviours.

**Practical Mental Model:** Treat Scalability as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes scalability necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Headroom and responsiveness versus infrastructure cost, complexity and premature optimisation.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add scalability” without requirements, constraints, acceptance evidence or review triggers.
- They should also understand that scaling is not simply "add more servers." Instances may disappear during scale-in, long-running jobs may need checkpoints, and work may need queues so another worker can continue processing.

**AI-Building Implications:** Make the Scalability decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Scalability to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a scalability decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** See the pillar index and adjacent production lifecycle components.

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04)

<details><summary>Recovered research synthesis</summary>

Students need vertical scaling, horizontal scaling, elasticity, stateless services, autoscaling, bottleneck identification and understanding that different parts of the application may scale differently.

   They should also understand that **scaling is not simply "add more servers."** Instances may disappear during scale-in, long-running jobs may need checkpoints, and work may need queues so another worker can continue processing. Microsoft specifically highlights those behaviours. 

   Advanced topics later include sharding, partitioning strategies, geographically distributed workloads and independent service scaling.

</details>

---

## P1-C10 — Load Balancing and Traffic Management

**Classification:** Should Know

**Core Principle:** Students should understand why multiple instances require traffic distribution, health checks, regional routing and failover.

**Why It Matters:** Load balancing also interacts with reliability, because incorrectly removing overloaded instances can push more traffic onto remaining instances and worsen an outage. Google documents this explicitly in its work on cascading failures.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about load balancing and traffic management, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Students should understand why multiple instances require traffic distribution, health checks, regional routing and failover.
- Load balancing also interacts with reliability, because incorrectly removing overloaded instances can push more traffic onto remaining instances and worsen an outage.
- Google documents this explicitly in its work on cascading failures.

**Practical Mental Model:** Treat Load Balancing and Traffic Management as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes load balancing and traffic management necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Headroom and responsiveness versus infrastructure cost, complexity and premature optimisation.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add load balancing and traffic management” without requirements, constraints, acceptance evidence or review triggers.
- Students should understand why multiple instances require traffic distribution, health checks, regional routing and failover.
- Google documents this explicitly in its work on cascading failures.

**AI-Building Implications:** Make the Load Balancing and Traffic Management decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Load Balancing and Traffic Management to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can recognise, explain and apply with guidance a load balancing and traffic management decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P6-C13 Load Testing; P2-C13 State Management; P2-C17 Dependency Management; P3-C38 Cognitive Load

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04)

<details><summary>Recovered research synthesis</summary>

Students should understand why multiple instances require traffic distribution, health checks, regional routing and failover. Load balancing also interacts with reliability, because incorrectly removing overloaded instances can push more traffic onto remaining instances and worsen an outage. Google documents this explicitly in its work on cascading failures.

</details>

---

## P1-C11 — Queues, Background Jobs and Event-Driven Architecture

**Classification:** Must Know

**Core Principle:** This is particularly important for AI applications.

**Why It Matters:** Students should understand when a request should complete immediately and when work should be moved behind the scenes. Examples include emails, document generation, video processing, AI generation, notifications, imports, scheduled tasks and large external API operations.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about queues, background jobs and event-driven architecture, then failing under real load, change or dependency loss.

**Concepts to Master:**

- This is particularly important for AI applications.
- Students should understand when a request should complete immediately and when work should be moved behind the scenes.
- Examples include emails, document generation, video processing, AI generation, notifications, imports, scheduled tasks and large external API operations.

**Practical Mental Model:** Treat Queues, Background Jobs and Event-Driven Architecture as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes queues, background jobs and event-driven architecture necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Responsiveness and decoupling versus ordering, retries, observability and operational complexity.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add queues, background jobs and event-driven architecture” without requirements, constraints, acceptance evidence or review triggers.
- They do not initially need Kafka internals.

**AI-Building Implications:** Make the Queues, Background Jobs and Event-Driven Architecture decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Queues, Background Jobs and Event-Driven Architecture to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a queues, background jobs and event-driven architecture decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P5-C24 Queues; P5-C25 Event-Driven Architecture; P5-C26 Scheduled Jobs / Cron; P5-C23 Background Workers

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02)

<details><summary>Recovered research synthesis</summary>

This is particularly important for AI applications.

   Students should understand when a request should complete immediately and when work should be moved behind the scenes. Examples include emails, document generation, video processing, AI generation, notifications, imports, scheduled tasks and large external API operations.

   Core concepts should include queues, producers, consumers/workers, retries, dead-letter handling, idempotency, job states and eventually events/pub-sub.

   They do not initially need Kafka internals.

</details>

---

## P1-C12 — Concurrency, Consistency and Data Integrity

**Classification:** Should Know

**Core Principle:** When two users attempt to book the same room, buy the final unit or modify the same record, what happens?

**Why It Matters:** Students should understand transactions, race conditions, locking conceptually, optimistic concurrency, idempotency and strong vs eventual consistency. The important teaching question is: Which information in your application must always be immediately correct, and which information can become correct shortly afterwards?

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about concurrency, consistency and data integrity, then failing under real load, change or dependency loss.

**Concepts to Master:**

- When two users attempt to book the same room, buy the final unit or modify the same record, what happens?
- Students should understand transactions, race conditions, locking conceptually, optimistic concurrency, idempotency and strong vs eventual consistency.
- The important teaching question is: Which information in your application must always be immediately correct, and which information can become correct shortly afterwards?

**Practical Mental Model:** Treat Concurrency, Consistency and Data Integrity as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- When two users attempt to book the same room, buy the final unit or modify the same record, what happens?
- Which information in your application must always be immediately correct, and which information can become correct shortly afterwards?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add concurrency, consistency and data integrity” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Concurrency, Consistency and Data Integrity decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Concurrency, Consistency and Data Integrity to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can recognise, explain and apply with guidance a concurrency, consistency and data integrity decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P3-C20 Consistency & Standards; P6-C28 Data Protection; P1-C04 Data Architecture; P3-C52 Analytics & Behaviour Data

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02)

<details><summary>Recovered research synthesis</summary>

When two users attempt to book the same room, buy the final unit or modify the same record, what happens?

   Students should understand transactions, race conditions, locking conceptually, optimistic concurrency, idempotency and strong vs eventual consistency.

   The important teaching question is:

   **Which information in your application must always be immediately correct, and which information can become correct shortly afterwards?**

</details>

---

## P1-C13 — Availability

**Classification:** Must Know

**Core Principle:** Availability should move from "my app should never go down" to measurable targets.

**Why It Matters:** Students should understand uptime, SLAs, SLOs, redundancy, failure domains, single points of failure, multi-zone deployment, dependency availability and what additional "nines" actually cost. Google SRE explicitly argues against blindly aiming for 100% reliability because excessive reliability can increase cost and reduce development velocity.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about availability, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Availability should move from "my app should never go down" to measurable targets.
- Students should understand uptime, SLAs, SLOs, redundancy, failure domains, single points of failure, multi-zone deployment, dependency availability and what additional "nines" actually cost.
- Google SRE explicitly argues against blindly aiming for 100% reliability because excessive reliability can increase cost and reduce development velocity.

**Practical Mental Model:** Availability is a measured user outcome over time, not a promise that nothing will fail.

**Student Decision Questions:**

- Which user journey is protected and what counts as a successful attempt?
- What SLI and time window will measure it, and what SLO does the business require?
- Which component or dependency is the current single point of failure?
- How much error budget is acceptable and what happens when it is consumed?
- What cost and complexity would the next “nine” require?

**Trade-offs:** Higher continuity and faster recovery versus cost, operational complexity and slower change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add availability” without requirements, constraints, acceptance evidence or review triggers.
- Availability should move from "my app should never go down" to measurable targets.
- Students should understand uptime, SLAs, SLOs, redundancy, failure domains, single points of failure, multi-zone deployment, dependency availability and what additional "nines" actually cost.

**AI-Building Implications:** Make the Availability decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Availability to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a availability decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** See the pillar index and adjacent production lifecycle components.

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04)

<details><summary>Recovered research synthesis</summary>

Availability should move from "my app should never go down" to measurable targets.

   Students should understand uptime, SLAs, SLOs, redundancy, failure domains, single points of failure, multi-zone deployment, dependency availability and what additional "nines" actually cost.

   Google SRE explicitly argues against blindly aiming for 100% reliability because excessive reliability can increase cost and reduce development velocity.

</details>

---

## P1-C14 — Reliability and Resilience

**Classification:** Must Know

**Core Principle:** Availability alone isn't sufficient.

**Why It Matters:** A reliable system must behave correctly and predictably during failures. Teach retries, exponential backoff, jitter, timeouts, circuit breakers, health checks, redundancy, graceful degradation, failover, bulkheads, recovery and fault isolation.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about reliability and resilience, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Availability alone isn't sufficient.
- A reliable system must behave correctly and predictably during failures.
- Teach retries, exponential backoff, jitter, timeouts, circuit breakers, health checks, redundancy, graceful degradation, failover, bulkheads, recovery and fault isolation.

**Practical Mental Model:** Treat Reliability and Resilience as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes reliability and resilience necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Higher continuity and faster recovery versus cost, operational complexity and slower change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add reliability and resilience” without requirements, constraints, acceptance evidence or review triggers.
- A reliable system must behave correctly and predictably during failures.
- Teach retries, exponential backoff, jitter, timeouts, circuit breakers, health checks, redundancy, graceful degradation, failover, bulkheads, recovery and fault isolation.

**AI-Building Implications:** Make the Reliability and Resilience decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Reliability and Resilience to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a reliability and resilience decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P6-C17 Reliability/Failure Testing; P7-C16 Production AI: Reliability, Latency & Cost; P2-C15 Defensive Programming; P5-C28 Integration Failure

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04)

<details><summary>Recovered research synthesis</summary>

Availability alone isn't sufficient. A reliable system must behave correctly and predictably during failures.

   Teach retries, exponential backoff, jitter, timeouts, circuit breakers, health checks, redundancy, graceful degradation, failover, bulkheads, recovery and fault isolation.

   This section should contain one of our most important production lessons:

   **Failures are normal. The design question is what happens next.**

   Microsoft explicitly recommends self-healing, redundancy and failure-mode analysis, while Google demonstrates how uncontrolled retries and overload can trigger cascading failures.

</details>

---

## P1-C15 — Overload Protection

**Classification:** Must Know

**Core Principle:** I would give this its own section rather than hiding it under scalability.

**Why It Matters:** Students should understand rate limiting, quotas, backpressure conceptually, request rejection, load shedding, queuing, timeouts, graceful degradation and capacity limits. Google describes overload as a major cause of cascading failure and recommends testing beyond expected capacity to learn how a service actually fails.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about overload protection, then failing under real load, change or dependency loss.

**Concepts to Master:**

- I would give this its own section rather than hiding it under scalability.
- Students should understand rate limiting, quotas, backpressure conceptually, request rejection, load shedding, queuing, timeouts, graceful degradation and capacity limits.
- Google describes overload as a major cause of cascading failure and recommends testing beyond expected capacity to learn how a service actually fails.

**Practical Mental Model:** Treat Overload Protection as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes overload protection necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Headroom and responsiveness versus infrastructure cost, complexity and premature optimisation.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add overload protection” without requirements, constraints, acceptance evidence or review triggers.
- Google describes overload as a major cause of cascading failure and recommends testing beyond expected capacity to learn how a service actually fails.

**AI-Building Implications:** Make the Overload Protection decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Overload Protection to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a overload protection decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P6-C28 Data Protection; P6-C26 Injection Protection; P5-C14 OAuth; P6-C22 Authentication Testing

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04)

<details><summary>Recovered research synthesis</summary>

I would give this its own section rather than hiding it under scalability.

   Students should understand rate limiting, quotas, backpressure conceptually, request rejection, load shedding, queuing, timeouts, graceful degradation and capacity limits.

   Google describes overload as a major cause of cascading failure and recommends testing beyond expected capacity to learn how a service actually fails. 

   Imagine an AI application receiving 50 times its normal prompt traffic. Instead of allowing every request to exhaust the database, model API and application servers, the system must protect itself.

</details>

---

## P1-C16 — Security Architecture

**Classification:** Must Know

**Core Principle:** Security must be part of the architecture, not something students "add before launch." Teach authentication vs authorisation, least privilege, role/permission models, row-level access, secrets, encryption in transit/at rest, input validation, dependency security, secure configuration, data classification, logging sensitive information, rate limiting, network boundaries and threat modelling.

**Why It Matters:** OWASP's current web Top 10 includes broken access control, security misconfiguration, software supply-chain failures, cryptographic failures, injection, insecure design and authentication failures.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about security architecture, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Security must be part of the architecture, not something students "add before launch." Teach authentication vs authorisation, least privilege, role/permission models, row-level access, secrets, encryption in transit/at rest, input valida…
- OWASP's current web Top 10 includes broken access control, security misconfiguration, software supply-chain failures, cryptographic failures, injection, insecure design and authentication failures.

**Practical Mental Model:** Treat Security Architecture as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes security architecture necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** More protection and containment versus user friction, integration effort and reduced autonomy.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add security architecture” without requirements, constraints, acceptance evidence or review triggers.
- Security must be part of the architecture, not something students "add before launch." Teach authentication vs authorisation, least privilege, role/permission models, row-level access, secrets, encryption in transit/at rest, input validation, dependency security, secure configuration, data classification, logging sensitive information, rate limiting, network boundaries and threat modelling.
- OWASP's current web Top 10 includes broken access control, security misconfiguration, software supply-chain failures, cryptographic failures, injection, insecure design and authentication failures.

**AI-Building Implications:** Make the Security Architecture decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Security Architecture to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a security architecture decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P6-C34 Security Testing; P7-C14 AI Security & Guardrails; P1-C17 API Security; P6-C27 Secrets Security

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-05](source-register.md#sys-05), [API-01](source-register.md#api-01), [API-02](source-register.md#api-02)

<details><summary>Recovered research synthesis</summary>

Security must be part of the architecture, not something students "add before launch."

   Teach authentication vs authorisation, least privilege, role/permission models, row-level access, secrets, encryption in transit/at rest, input validation, dependency security, secure configuration, data classification, logging sensitive information, rate limiting, network boundaries and threat modelling.

   OWASP's current web Top 10 includes broken access control, security misconfiguration, software supply-chain failures, cryptographic failures, injection, insecure design and authentication failures.

</details>

---

## P1-C17 — API Security

**Classification:** Must Know

**Core Principle:** I would separate this from general security because modern AI-built products rely so heavily on APIs.

**Why It Matters:** OWASP's API Top 10 includes broken object-level authorisation, broken authentication, unrestricted resource consumption, broken function-level authorisation, sensitive business-flow abuse, SSRF, inventory problems and unsafe consumption of third-party APIs. The practical Builders Academy test is simple: Can User A manipulate an ID or API request and see User B's data?

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about api security, then failing under real load, change or dependency loss.

**Concepts to Master:**

- I would separate this from general security because modern AI-built products rely so heavily on APIs.
- OWASP's API Top 10 includes broken object-level authorisation, broken authentication, unrestricted resource consumption, broken function-level authorisation, sensitive business-flow abuse, SSRF, inventory problems and unsafe consumption …
- The practical Builders Academy test is simple: Can User A manipulate an ID or API request and see User B's data?

**Practical Mental Model:** Treat API Security as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes api security necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** More protection and containment versus user friction, integration effort and reduced autonomy.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add api security” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the API Security decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply API Security to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a api security decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P4-C14 API vs MCP; P5-C02 API Fundamentals; P5-C05 API Contracts; P5-C06 API Documentation

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [API-01](source-register.md#api-01), [API-02](source-register.md#api-02), [API-05](source-register.md#api-05)

<details><summary>Recovered research synthesis</summary>

I would separate this from general security because modern AI-built products rely so heavily on APIs.

   OWASP's API Top 10 includes broken object-level authorisation, broken authentication, unrestricted resource consumption, broken function-level authorisation, sensitive business-flow abuse, SSRF, inventory problems and unsafe consumption of third-party APIs. 

   The practical Builders Academy test is simple:

   **Can User A manipulate an ID or API request and see User B's data?**

   If yes, the application's beautiful login screen means very little.

</details>

---

## P1-C18 — Third-Party Dependencies

**Classification:** Must Know

**Core Principle:** Products increasingly depend on Supabase, Stripe, OpenAI, Resend, Twilio, authentication providers, maps, analytics and dozens of other services.

**Why It Matters:** Students need dependency mapping, timeout/retry behaviour, fallback behaviour, quotas, rate limits, API-version changes, vendor outages, cost exposure and vendor lock-in considerations. Ask: If this service disappears for 30 minutes, what happens to my application?

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about third-party dependencies, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Products increasingly depend on Supabase, Stripe, OpenAI, Resend, Twilio, authentication providers, maps, analytics and dozens of other services.
- Students need dependency mapping, timeout/retry behaviour, fallback behaviour, quotas, rate limits, API-version changes, vendor outages, cost exposure and vendor lock-in considerations.
- Ask: If this service disappears for 30 minutes, what happens to my application?

**Practical Mental Model:** Treat Third-Party Dependencies as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes third-party dependencies necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add third-party dependencies” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Third-Party Dependencies decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Third-Party Dependencies to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a third-party dependencies decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P5-C27 Third-Party Services; P6-C12 Performance Testing; P2-C15 Defensive Programming; P2-C28 Refactoring Patterns & Code Smells

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [API-05](source-register.md#api-05)

<details><summary>Recovered research synthesis</summary>

Products increasingly depend on Supabase, Stripe, OpenAI, Resend, Twilio, authentication providers, maps, analytics and dozens of other services.

   Students need dependency mapping, timeout/retry behaviour, fallback behaviour, quotas, rate limits, API-version changes, vendor outages, cost exposure and vendor lock-in considerations.

   **Ask:** If this service disappears for 30 minutes, what happens to my application?

</details>

---

## P1-C19 — Observability

**Classification:** Must Know

**Core Principle:** Students need logs, metrics, traces, dashboards, alerts and error tracking conceptually.

**Why It Matters:** But observability should start with user-visible outcomes rather than dashboards full of meaningless metrics. Google SRE recommends SLIs/SLOs for identifying whether the service is actually meeting user expectations and then deeper operational metrics for diagnosing why it is not.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about observability, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Students need logs, metrics, traces, dashboards, alerts and error tracking conceptually.
- But observability should start with user-visible outcomes rather than dashboards full of meaningless metrics.
- Google SRE recommends SLIs/SLOs for identifying whether the service is actually meeting user expectations and then deeper operational metrics for diagnosing why it is not.

**Practical Mental Model:** Treat Observability as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes observability necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add observability” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Observability decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Observability to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a observability decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P4-C33 Observability for Agents; P5-C38 API Observability; P7-C15 Evals, Tracing & AI Observability; P4-C29 Agent Harnesses

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-05](source-register.md#sys-05)

<details><summary>Recovered research synthesis</summary>

Students need logs, metrics, traces, dashboards, alerts and error tracking conceptually.

   But observability should start with user-visible outcomes rather than dashboards full of meaningless metrics. Google SRE recommends SLIs/SLOs for identifying whether the service is actually meeting user expectations and then deeper operational metrics for diagnosing why it is not. 

   Students should learn the difference between:

   **"The server is running."**

   and

   **"Customers can successfully complete checkout."**

</details>

---

## P1-C20 — SLI, SLO and SLA

**Classification:** Must Know

**Core Principle:** This could become one of Builders Academy's differentiators.

**Why It Matters:** Students should define measurable expectations for their important flows: Availability: 99.9%. Latency: 95% of requests under 500 ms.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about sli, slo and sla, then failing under real load, change or dependency loss.

**Concepts to Master:**

- This could become one of Builders Academy's differentiators.
- Students should define measurable expectations for their important flows: Availability: 99.9%.
- Latency: 95% of requests under 500 ms.

**Practical Mental Model:** Treat SLI, SLO and SLA as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes sli, slo and sla necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add sli, slo and sla” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the SLI, SLO and SLA decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply SLI, SLO and SLA to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a sli, slo and sla decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P2-C21 Technical Debt; P3-C35 Perceived Performance; P6-C14 Stress Testing; P6-C16 Soak Testing

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04)

<details><summary>Recovered research synthesis</summary>

This could become one of Builders Academy's differentiators.

   Students should define measurable expectations for their important flows:

   **Availability:** 99.9%.

   **Latency:** 95% of requests under 500 ms.

   **Correctness:** 99.99% successful payment recording.

   **Freshness:** dashboard data updated within 60 seconds.

   Google describes SLIs as measurements, SLOs as their target values, and recommends choosing them according to behaviour users actually care about.

</details>

---

## P1-C21 — Backups, Disaster Recovery and Business Continuity

**Classification:** Must Know

**Core Principle:** Students need backups, restore testing, data-loss tolerance, recovery-time tolerance, RPO, RTO, regional failure conceptually and dependency recovery.

**Why It Matters:** Microsoft describes reliable workloads as needing both resilience during disruption and recoverability within defined time and data-loss limits. The most useful questions are: How much data could you afford to lose?

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about backups, disaster recovery and business continuity, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Students need backups, restore testing, data-loss tolerance, recovery-time tolerance, RPO, RTO, regional failure conceptually and dependency recovery.
- Microsoft describes reliable workloads as needing both resilience during disruption and recoverability within defined time and data-loss limits.
- The most useful questions are: How much data could you afford to lose?

**Practical Mental Model:** Treat Backups, Disaster Recovery and Business Continuity as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- How much data could you afford to lose?
- How long could your product remain unavailable?

**Trade-offs:** Higher continuity and faster recovery versus cost, operational complexity and slower change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add backups, disaster recovery and business continuity” without requirements, constraints, acceptance evidence or review triggers.
- Students need backups, restore testing, data-loss tolerance, recovery-time tolerance, RPO, RTO, regional failure conceptually and dependency recovery.

**AI-Building Implications:** Make the Backups, Disaster Recovery and Business Continuity decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Backups, Disaster Recovery and Business Continuity to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a backups, disaster recovery and business continuity decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P6-C48 Business Monitoring; P2-C07 DRY, But Not Blindly; P2-C25 Documentation; P2-C28 Refactoring Patterns & Code Smells

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04), [API-01](source-register.md#api-01)

<details><summary>Recovered research synthesis</summary>

Students need backups, restore testing, data-loss tolerance, recovery-time tolerance, RPO, RTO, regional failure conceptually and dependency recovery.

   Microsoft describes reliable workloads as needing both resilience during disruption and recoverability within defined time and data-loss limits. 

   The most useful questions are:

   **How much data could you afford to lose?**

   **How long could your product remain unavailable?**

</details>

---

## P1-C22 — Deployments and Change Safety

**Classification:** Must Know

**Core Principle:** Many outages happen because something changed.

**Why It Matters:** Teach environments, development/staging/production separation, CI/CD conceptually, database migrations, feature flags, rollback, version compatibility, environment variables, secrets management, deployment health checks and safe releases. Operational excellence is explicitly treated as a foundational architecture concern by AWS, rather than merely an operations concern after development.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about deployments and change safety, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Many outages happen because something changed.
- Teach environments, development/staging/production separation, CI/CD conceptually, database migrations, feature flags, rollback, version compatibility, environment variables, secrets management, deployment health checks and safe releases.
- Operational excellence is explicitly treated as a foundational architecture concern by AWS, rather than merely an operations concern after development.

**Practical Mental Model:** Treat Deployments and Change Safety as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes deployments and change safety necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add deployments and change safety” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Deployments and Change Safety decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Deployments and Change Safety to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a deployments and change safety decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P6-C39 Database Migration Safety; P6-C35 Vulnerability Management; P2-C01 Simplicity; P2-C04 High Cohesion, Low Coupling

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SE-03](source-register.md#se-03), [SEC-01](source-register.md#sec-01), [SEC-02](source-register.md#sec-02)

<details><summary>Recovered research synthesis</summary>

Many outages happen because something changed.

   Teach environments, development/staging/production separation, CI/CD conceptually, database migrations, feature flags, rollback, version compatibility, environment variables, secrets management, deployment health checks and safe releases.

   Operational excellence is explicitly treated as a foundational architecture concern by AWS, rather than merely an operations concern after development.

</details>

---

## P1-C23 — Testing the Architecture

**Classification:** Must Know

**Core Principle:** Students should eventually test functional behaviour, API behaviour, integration, end-to-end flows, load, failure, recovery, permissions, cross-user data isolation and backups.

**Why It Matters:** Google emphasises testing services at and beyond overload thresholds because failure behaviour is difficult to predict purely from architecture diagrams.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about testing the architecture, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Students should eventually test functional behaviour, API behaviour, integration, end-to-end flows, load, failure, recovery, permissions, cross-user data isolation and backups.
- Google emphasises testing services at and beyond overload thresholds because failure behaviour is difficult to predict purely from architecture diagrams.

**Practical Mental Model:** Specify expected behaviour, create evidence, run the check, inspect failures, then prevent regression.

**Student Decision Questions:**

- What user or production requirement makes testing the architecture necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** More confidence and safer change versus maintenance cost, execution time and brittle test design.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add testing the architecture” without requirements, constraints, acceptance evidence or review triggers.
- Students should eventually test functional behaviour, API behaviour, integration, end-to-end flows, load, failure, recovery, permissions, cross-user data isolation and backups.
- Google emphasises testing services at and beyond overload thresholds because failure behaviour is difficult to predict purely from architecture diagrams.

**AI-Building Implications:** Make the Testing the Architecture decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Testing the Architecture to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a testing the architecture decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P2-C19 Testing as a Design Practice; P6-C01 Testing Mindset; P6-C06 Unit Testing; P6-C08 End-to-End Testing

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04)

<details><summary>Recovered research synthesis</summary>

Not just unit tests.

   Students should eventually test functional behaviour, API behaviour, integration, end-to-end flows, load, failure, recovery, permissions, cross-user data isolation and backups.

   Google emphasises testing services at and beyond overload thresholds because failure behaviour is difficult to predict purely from architecture diagrams.

</details>

---

## P1-C24 — Cost Architecture

**Classification:** Must Know

**Core Principle:** A system can technically scale and financially destroy the business.

**Why It Matters:** Teach compute cost, database cost, storage, bandwidth/egress, API usage, AI/token cost, logging, backups and per-user/per-transaction economics. AWS treats cost optimisation as a first-class architecture pillar and explicitly frames architectural choices as trade-offs driven by business requirements.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about cost architecture, then failing under real load, change or dependency loss.

**Concepts to Master:**

- A system can technically scale and financially destroy the business.
- Teach compute cost, database cost, storage, bandwidth/egress, API usage, AI/token cost, logging, backups and per-user/per-transaction economics.
- AWS treats cost optimisation as a first-class architecture pillar and explicitly frames architectural choices as trade-offs driven by business requirements.

**Practical Mental Model:** Treat Cost Architecture as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes cost architecture necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Capability and quality versus latency, unit economics, privacy constraints and provider dependence.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add cost architecture” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Cost Architecture decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Cost Architecture to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a cost architecture decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P4-C34 Cost Management; P7-C16 Production AI: Reliability, Latency & Cost; P4-C33 Observability for Agents; P5-C21 Server vs Serverless

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04), [SYS-05](source-register.md#sys-05)

<details><summary>Recovered research synthesis</summary>

A system can technically scale and financially destroy the business.

   Teach compute cost, database cost, storage, bandwidth/egress, API usage, AI/token cost, logging, backups and per-user/per-transaction economics.

   AWS treats cost optimisation as a first-class architecture pillar and explicitly frames architectural choices as trade-offs driven by business requirements. 

   AI makes this particularly important.

   **What does one active user cost you?**

</details>

---

## P1-C25 — Architecture Evolution and Maintainability

**Classification:** Must Know

**Core Principle:** Students need to understand technical debt, loose coupling, component boundaries, API versioning, schema migration, replacing dependencies and avoiding premature complexity.

**Why It Matters:** Microsoft's guidance explicitly identifies "design for evolution" as a strategic principle.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about architecture evolution and maintainability, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Students need to understand technical debt, loose coupling, component boundaries, API versioning, schema migration, replacing dependencies and avoiding premature complexity.
- Microsoft's guidance explicitly identifies "design for evolution" as a strategic principle.

**Practical Mental Model:** Treat Architecture Evolution and Maintainability as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes architecture evolution and maintainability necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add architecture evolution and maintainability” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Architecture Evolution and Maintainability decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Architecture Evolution and Maintainability to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a architecture evolution and maintainability decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P2-C30 Evolutionary Design

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02)

<details><summary>Recovered research synthesis</summary>

Systems change. Students need to understand technical debt, loose coupling, component boundaries, API versioning, schema migration, replacing dependencies and avoiding premature complexity.

   Microsoft's guidance explicitly identifies "design for evolution" as a strategic principle.

</details>

---

## P1-C26 — Multi-tenancy

**Classification:** Should Know

**Core Principle:** Tenant isolation, shared vs dedicated resources, tenant IDs, permissions, storage isolation, noisy neighbours, quotas and per-tenant configuration become highly relevant to SaaS platforms.

**Why It Matters:** It changes whether the product remains understandable, safe and operable when real users and real data are involved.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about multi-tenancy, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Tenant isolation, shared vs dedicated resources, tenant IDs, permissions, storage isolation, noisy neighbours, quotas and per-tenant configuration become highly relevant to SaaS platforms.

**Practical Mental Model:** Treat Multi-tenancy as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes multi-tenancy necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add multi-tenancy” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Multi-tenancy decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Multi-tenancy to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can recognise, explain and apply with guidance a multi-tenancy decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** See the pillar index and adjacent production lifecycle components.

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02)

<details><summary>Recovered research synthesis</summary>

Tenant isolation, shared vs dedicated resources, tenant IDs, permissions, storage isolation, noisy neighbours, quotas and per-tenant configuration become highly relevant to SaaS platforms.

</details>

---

## P1-C27 — Geographic and Global Architecture

**Classification:** Should Know

**Core Principle:** Regions, availability zones, latency by geography, CDN, data residency, multi-region deployment, replication and localisation.

**Why It Matters:** Advanced: global writes, active-active architectures, distributed consensus and complex cross-region consistency.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about geographic and global architecture, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Regions, availability zones, latency by geography, CDN, data residency, multi-region deployment, replication and localisation.
- Advanced: global writes, active-active architectures, distributed consensus and complex cross-region consistency.

**Practical Mental Model:** Treat Geographic and Global Architecture as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes geographic and global architecture necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add geographic and global architecture” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Geographic and Global Architecture decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Geographic and Global Architecture to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can recognise, explain and apply with guidance a geographic and global architecture decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P5-C22 Edge Functions

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04)

<details><summary>Recovered research synthesis</summary>

Regions, availability zones, latency by geography, CDN, data residency, multi-region deployment, replication and localisation.

   **Advanced:** global writes, active-active architectures, distributed consensus and complex cross-region consistency.

</details>

---

## P1-C28 — Realtime Systems

**Classification:** Should Know

**Core Principle:** Polling, WebSockets, Server-Sent Events, pub/sub, presence, notification systems and reconnect behaviour.

**Why It Matters:** Not every app needs realtime architecture.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about realtime systems, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Polling, WebSockets, Server-Sent Events, pub/sub, presence, notification systems and reconnect behaviour.
- Not every app needs realtime architecture.

**Practical Mental Model:** Treat Realtime Systems as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes realtime systems necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Responsiveness and decoupling versus ordering, retries, observability and operational complexity.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add realtime systems” without requirements, constraints, acceptance evidence or review triggers.
- Not every app needs realtime architecture.

**AI-Building Implications:** Make the Realtime Systems decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Realtime Systems to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can recognise, explain and apply with guidance a realtime systems decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P5-C16 Polling vs Webhooks vs Realtime; P5-C17 WebSockets & Realtime; P5-C18 Database as Infrastructure

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02)

<details><summary>Recovered research synthesis</summary>

Polling, WebSockets, Server-Sent Events, pub/sub, presence, notification systems and reconnect behaviour.

   Not every app needs realtime architecture.

</details>

---

## P1-C29 — Search Architecture

**Classification:** Should Know

**Core Principle:** Database search vs dedicated search engines, indexing, full-text search, autocomplete, filtering, ranking and eventually semantic/vector search for AI applications.

**Why It Matters:** It changes whether the product remains understandable, safe and operable when real users and real data are involved.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about search architecture, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Database search vs dedicated search engines, indexing, full-text search, autocomplete, filtering, ranking and eventually semantic/vector search for AI applications.

**Practical Mental Model:** Treat Search Architecture as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes search architecture necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add search architecture” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Search Architecture decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Search Architecture to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can recognise, explain and apply with guidance a search architecture decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P5-C07 Pagination, Filtering, Sorting & Search; P2-C03 Modularity; P3-C03 Information Architecture; P3-C15 Empty States

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [AI-09](source-register.md#ai-09)

<details><summary>Recovered research synthesis</summary>

Database search vs dedicated search engines, indexing, full-text search, autocomplete, filtering, ranking and eventually semantic/vector search for AI applications.

</details>

---

## P1-C30 — Architecture Documentation and Decision Records

**Classification:** Must Know

**Core Principle:** Every Builders Academy student should leave able to document why an architectural choice exists.

**Why It Matters:** Instead of: "We're using Redis." We want: "Repeated catalogue reads dominate our workload, so we will introduce cache-aside caching with a five-minute staleness tolerance to reduce database pressure." That is engineering judgment.

**Production Problem Solved:** Prevents a production system from relying on unmeasured assumptions about architecture documentation and decision records, then failing under real load, change or dependency loss.

**Concepts to Master:**

- Every Builders Academy student should leave able to document why an architectural choice exists.
- Instead of: "We're using Redis." We want: "Repeated catalogue reads dominate our workload, so we will introduce cache-aside caching with a five-minute staleness tolerance to reduce database pressure." That is engineering judgment.

**Practical Mental Model:** Treat Architecture Documentation and Decision Records as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes architecture documentation and decision records necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add architecture documentation and decision records” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Architecture Documentation and Decision Records decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Architecture Documentation and Decision Records to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: a diagram or decision record plus measured load, failure or SLO evidence. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a architecture documentation and decision records decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P2-C26 Architecture Decision Records; P2-C25 Documentation; P5-C06 API Documentation; P4-C24 Memory

**Authoritative Research Sources:** [SYS-01](source-register.md#sys-01), [SYS-02](source-register.md#sys-02), [API-04](source-register.md#api-04)

<details><summary>Recovered research synthesis</summary>

Every Builders Academy student should leave able to document **why** an architectural choice exists.

   Instead of:

   *"We're using Redis."*

   We want:

   *"Repeated catalogue reads dominate our workload, so we will introduce cache-aside caching with a five-minute staleness tolerance to reduce database pressure."*

   That is engineering judgment.

</details>

---

