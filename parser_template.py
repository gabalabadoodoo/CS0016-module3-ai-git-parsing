"""Module 3 combined lab starter.

Complete each function with help from an approved AI tool, then verify every
claim and code change using the supplied unit tests. The files contain only
fictional classroom data.
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml


def parse_xml(path: str | Path) -> dict:
    """Return default_operation and test_option from the NETCONF-style XML."""
    tree = ET.parse(path)
    root = tree.getroot()

    namespaces = {
        "nc": "urn:ietf:params:xml:ns:netconf:base:1.0"
    }

    default_operation = root.findtext(
        "nc:edit-config/nc:default-operation",
        namespaces=namespaces,
    )
    test_option = root.findtext(
        "nc:edit-config/nc:test-option",
        namespaces=namespaces,
    )

    if default_operation is None or test_option is None:
        raise ValueError("Required NETCONF XML elements are missing")

    return {
        "default_operation": default_operation,
        "test_option": test_option,
    }


def parse_json(path: str | Path) -> dict:
    """Return site, device_count, enabled_devices, and roles from the JSON."""
    with Path(path).open(encoding="utf-8") as file:
        data = json.load(file)

    devices = data["devices"]

    return {
        "site": data["site"],
        "device_count": len(devices),
        "enabled_devices": [
            device["hostname"]
            for device in devices
            if device["enabled"]
        ],
        "roles": [
            device["role"]
            for device in devices
        ],
    }


def parse_yaml(path: str | Path) -> dict:
    """Return name, approved, duration_minutes, devices, and action from YAML."""
    # TODO: use yaml.safe_load and return the normalized maintenance summary.
    raise NotImplementedError("Complete parse_yaml")


def build_summary(xml_path: str | Path, json_path: str | Path, yaml_path: str | Path) -> dict:
    """Combine the three parser results into one dictionary."""
    # TODO: call the three parser functions and preserve the keys below.
    raise NotImplementedError("Complete build_summary")


if __name__ == "__main__":
    base = Path(__file__).resolve().parent
    summary = build_summary(
        base / "network_config.xml",
        base / "devices.json",
        base / "maintenance.yaml",
    )
    print(json.dumps(summary, indent=2))
