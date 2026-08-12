import json
import os
import sys
from pathlib import Path


def metadata(primary, legacy, default):
    return os.environ.get(primary) or os.environ.get(legacy, default)


PLACEHOLDERS = {
    "{{RESUKISU_VERSION}}": lambda: metadata(
        "RESUKISU_VERSION", "KSU_VERSION", "unknown"
    ),
    "{{RESUKISU_GIT_TAG}}": lambda: metadata(
        "RESUKISU_GIT_TAG", "KSU_GIT_TAG", "no-tag"
    ),
    "{{RESUKISU_BRANCH}}": lambda: metadata(
        "RESUKISU_BRANCH", "KSUN_BRANCH", "main"
    ),
    "{{RESUKISU_COMMIT}}": lambda: metadata(
        "RESUKISU_COMMIT", "KSUN_COMMIT", "unknown"
    ),
    "{{RESUKISU_MANAGER}}": lambda: metadata(
        "RESUKISU_MANAGER", "KSU_MANAGER", "Unavailable"
    ),
    # Backward-compatible placeholders for older release templates.
    "{{KSU_VERSION}}": lambda: metadata(
        "RESUKISU_VERSION", "KSU_VERSION", "unknown"
    ),
    "{{KSU_GIT_TAG}}": lambda: metadata(
        "RESUKISU_GIT_TAG", "KSU_GIT_TAG", "no-tag"
    ),
    "{{KSUN_BRANCH}}": lambda: metadata(
        "RESUKISU_BRANCH", "KSUN_BRANCH", "main"
    ),
    "{{KSUN_COMMIT}}": lambda: metadata(
        "RESUKISU_COMMIT", "KSUN_COMMIT", "unknown"
    ),
    "{{KSU_MANAGER}}": lambda: metadata(
        "RESUKISU_MANAGER", "KSU_MANAGER", "Unavailable"
    ),
    "{{SUSFS_BRANCHES}}": lambda: os.environ.get(
        "SUSFS_COMMIT", "latest on auto-derived gki-{version} branch"
    ),
    "{{SUSFS_BRANCHS}}": lambda: os.environ.get(
        "SUSFS_COMMIT", "latest on auto-derived gki-{version} branch"
    ),
}


def render_markdown(template_path: Path):
    text = template_path.read_text()

    for placeholder, getter in PLACEHOLDERS.items():
        text = text.replace(placeholder, getter())

    print(text, end="")


config_path = Path(sys.argv[1])
if config_path.suffix.lower() == ".md":
    render_markdown(config_path)
    sys.exit(0)

# Backward-compatible JSON renderer for older release configs.

def emit(text=""):
    print(text)


def emit_list(items):
    if isinstance(items, list):
        for item in items:
            emit(f"- {item}")


def emit_description(value):
    if isinstance(value, list):
        for line in value:
            emit(line)
    elif value:
        emit(str(value))


data = json.loads(config_path.read_text())

emit("**IMPORTANT DISCLAIMER**")
for line in data["release"]["disclaimer"]:
    emit(line)

resukisu = data.get("resukisu", data.get("kernelsu", {}))
emit()
emit(f"## {resukisu.get('name', 'ReSukiSU')}")
version = metadata(
    "RESUKISU_VERSION", "KSU_VERSION", resukisu.get("version", "unknown")
)
tag = metadata(
    "RESUKISU_GIT_TAG", "KSU_GIT_TAG", resukisu.get("tag", "no-tag")
)
branch = metadata(
    "RESUKISU_BRANCH", "KSUN_BRANCH", resukisu.get("branch", "main")
)
commit = metadata(
    "RESUKISU_COMMIT", "KSUN_COMMIT", resukisu.get("commit", "unknown")
)
emit(f"- Version: {version}")
emit(f"- Tag: {tag}")
emit(f"- Branch: {branch}")
emit(f"- Commit: {commit}")
if resukisu.get("url"):
    emit(f"- URL: {resukisu['url']}")
if resukisu.get("manager"):
    emit(f"- Manager: {resukisu['manager']}")

skip_keys = {"release", "resukisu", "kernelsu"}
for key in data.keys():
    if key in skip_keys:
        continue

    section = data[key]
    emit()
    emit(f"## {section.get('name', key)}")

    if section.get("description"):
        emit_description(section["description"])

    if section.get("version"):
        emit(f"- Version: {section['version']}")
    if section.get("tag"):
        emit(f"- Tag: {section['tag']}")
    if section.get("branch"):
        emit(f"- Branch: {section['branch']}")

    if key == "susfs":
        susfs_commit = os.environ.get("SUSFS_COMMIT", "")
        if susfs_commit:
            emit(f"- Commit: `{susfs_commit}`")
        else:
            emit("- Commit: latest on auto-derived gki-{version} branch")

    if section.get("items"):
        emit_list(section["items"])

    if section.get("url"):
        emit(f"- URL: {section['url']}")
