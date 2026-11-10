> Update, 10 November 2026: the owner explicitly approved making the repository public and publishing the prepared release. Earlier private-review restrictions below describe the prior review stage and are superseded for this release.

# Private review delivery and publication gates

Approved repository: `Beckleytobi/boteco-engineering-skills`, PRIVATE.
Approved branch: main. Release tag: fr4-claude-tested-licensed-r1. Release state: DRAFT prerelease.

The user authorized repository creation, source upload and draft release assets. They explicitly withheld publication. The CLI account was verified before creation; no existing repository was found under this name.

1. Upload the reviewed source using the configured Git identity and record its exact commit SHA.
2. Create a draft prerelease against that commit, attaching the unchanged licensed ZIP and SHA256SUMS.txt. Verify repository privacy, draft state and downloaded checksums independently.
3. Give the owner the private repository and draft URLs. Only eligible signed-in reviewers can access them; a private draft is not a public download.
4. Keep both repository and release private/unpublished. Any public visibility change or publication requires separate explicit approval. No automatic publishing workflow is included.
5. If a discrepancy is found, stop before publication and correct the draft under authorized scope. Never silently replace a published artifact; already downloaded copies cannot be recalled.

Local validation does not imply enforced GitHub branch rules. No branch protections or CI runs are claimed. No production deployment occurs.

Reference: [GitHub release management](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
