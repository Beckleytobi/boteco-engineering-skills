# Artifacts, deployment, verification, and recovery

Use this reference after CI or whenever build/deploy/rollback behavior is being designed or evaluated.

## Build and artifact governance

Where the platform supports it, build once and promote the same verified artifact. Record commit SHA, artifact digest or immutable ID, build/run ID, version, source branch, and target environment. If an environment rebuilds from source, state that the deployed bytes differ from the tested artifact and compensate proportionately.

Do not publish or promote an artifact whose required build, provenance, integrity, or security evidence is missing.

## Environments

Use only environments justified by risk and project maturity:

- development: active engineering;
- preview: change-specific inspection;
- staging: production-like verification;
- production: real users/data/consequences.

State material differences between validation and production. Never claim staging proves production behavior when data, topology, configuration, dependencies, or scale differ materially.

## Strategy selection

Choose standard, rolling, blue-green, canary, or feature-flag rollout based on blast radius, traffic, architecture, cost, observability, and recovery. Complexity must purchase a concrete risk reduction.

Before production, define:

- deploy identity and authorized actor;
- target environment and current known-good version;
- migration/order dependencies;
- concurrency behavior;
- rollout steps and stop conditions;
- health, smoke, and critical-journey checks;
- monitoring signals and observation window;
- rollback, roll-forward, or containment action.

## Concurrency

Concurrent deployment can corrupt state or make causality and rollback ambiguous. For the same stateful environment, use one of:

- serialized deployment;
- safe cancellation of a superseded run;
- isolated slots/environments with atomic promotion;
- a platform-specific strategy whose interaction is verified.

Do not start another production mutation while the previous one is in an uncertain state.

Treat an unresolved concurrency conflict involving the same production database or stateful environment as `HIGH` delivery risk unless verified isolation makes the blast radius materially smaller.

## Deployment is not health

After a successful deploy command, independently evaluate application-specific signals such as:

- process/readiness and critical dependency connectivity;
- critical APIs and user journeys, including authentication when relevant;
- migration/postcondition checks;
- worker/queue health;
- error rate, latency, saturation, and business signals;
- unexpected security or data-integrity symptoms.

Use a risk-proportionate observation window. Record `NOT RUN` or `UNKNOWN` for unavailable checks.

## Recovery

Before significant production delivery, identify the previous known-good artifact/configuration, restore or rollback mechanism, database compatibility, irreversible changes, feature-flag/traffic controls, expected recovery time, verification after recovery, and authority to invoke it.

For database changes, rollback may be unsafe; a rehearsed roll-forward or expand/contract path can be the valid recovery strategy. “We can redeploy” is not evidence unless the artifact and procedure are available.

## Stop and rollback conditions

Examples include failed health/critical journey, material error or latency increase, data-integrity failure, migration failure, security signal, or unexplained divergence from baseline. On a stop condition: halt rollout, preserve evidence, choose the authorized recovery action, verify recovered health, and keep the incident/change open until state is known.

Report two layers explicitly when a post-deploy check fails:

- the affected gate, such as `Post-deploy health: FAIL`;
- the overall delivery decision, `BLOCKED`, with rollback/recovery as the next safe action.

Do not call the release complete merely because the deploy command returned success.
