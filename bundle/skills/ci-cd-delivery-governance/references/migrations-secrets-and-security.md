# Migrations, secrets, and security-sensitive delivery

Use this reference when delivery touches persistent data, credentials, privileged workflows, infrastructure, or security controls.

## Database migration gates

Discover the migration tool, ordering model, transaction behavior, deployment sequence, production engine/version, data volume/shape, backup/recovery reality, and application-version compatibility.

For relevant changes evaluate:

- destructive drops, renames, type changes, nullability, and constraints;
- indexes and lock/downtime behavior;
- data backfills, batching, resume/idempotency, and observability;
- old/new application coexistence during rolling deploys;
- preflight checks against production-like existing data;
- post-migration invariants and query behavior;
- rollback, roll-forward, restore, or containment.

A migration that passes only on an empty database is insufficient when existing data can violate constraints, exceed timing limits, or trigger destructive behavior. Prefer expand/migrate/contract for high-risk compatibility changes when justified.

Block destructive or irreversible production migration when data-impact evidence, authority, or a credible recovery plan is missing.

## Secrets and environment configuration

Never place sensitive values in source, workflow YAML, command output, logs, artifacts, documentation, or PR comments. Use repository/environment/provider secret stores and least privilege.

Before a privileged job, verify required secret names/configuration exist without exposing their values, are scoped to the intended environment/job, are unavailable to untrusted code, and have only required permissions. A missing production secret is `BLOCKED`; inventing a fallback or printing secrets is not remediation.

If a secret is exposed:

1. stop further propagation;
2. do not repeat the value;
3. rotate/revoke through an authorized actor;
4. remove it from current code and artifacts;
5. assess history/log/cache exposure and follow repository policy;
6. independently verify remediation before delivery resumes.

Deleting the visible line alone does not make the leaked credential safe.

## Security-sensitive pipeline changes

Elevate changes involving workflow permissions, OIDC/cloud roles, third-party actions, self-hosted runners, artifact trust, environment protections, branch rules, scanners, signing/provenance, or dependency publishing.

Require independent review and explicit authority where a change expands privilege or weakens a control. The change must not approve itself. Prefer short-lived identity, minimal permissions, immutable artifacts, and verifiable provenance where risk justifies them.
