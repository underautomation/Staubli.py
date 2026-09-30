#!/usr/bin/env python3
"""
Runs the equivalent of:
    from underautomation.staubli.xxx import *
for every module and sub-package, found recursively.

Usage:
    python tests/test_import_all.py [package_name]

Examples:
    python tests/test_import_all.py
    python tests/test_import_all.py underautomation.staubli

Notes:
- The real import and the star import ("from X import *") are executed. This finds:
    * syntax errors,
    * missing imports,
    * names of __all__ that do not exist,
    * circular references raised at import time.
- Each star import runs in its own namespace, so the namespace of this script stays clean.
- Returns the exit code 1 when an import fails, 0 otherwise.
"""

import os
import sys
import pkgutil
import importlib
import traceback

def iter_modules_and_packages(package_name: str):
    """Yields every module and sub-package (recursively), the root package first."""
    yield package_name, True  # True = package (root)
    try:
        pkg = importlib.import_module(package_name)
    except Exception:
        # The root package cannot be imported: nothing more to walk
        return

    if not hasattr(pkg, "__path__"):
        # Not a package
        return

    for _, name, is_pkg in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
        yield name, is_pkg

def do_star_import(module_name: str):
    """
    Runs 'from module_name import *' in an isolated namespace.
    Raises an exception when the import fails.
    """
    ns = {}
    code = f"from {module_name} import *"
    exec(code, ns, ns)

def main():
    # Root of the repository in the path, to run it from the sources
    repo_root = os.path.abspath(".")
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

    package_name = sys.argv[1] if len(sys.argv) > 1 else "underautomation.staubli"

    failures = []
    tested = 0

    print(f"[INFO] 'import *' of every module of the package: {package_name}\n")

    for name, is_pkg in iter_modules_and_packages(package_name):
        tested += 1
        kind = "package" if is_pkg else "module"
        try:
            do_star_import(name)
            print(f"[OK] from {name} import *   ({kind})")
        except Exception as e:
            print(f"[FAIL] from {name} import *   ({kind})")
            failures.append((name, e, traceback.format_exc()))

    print("\n=== Summary ===")
    print(f"Tested: {tested}")
    print(f"Failures: {len(failures)}")

    if failures:
        print("\nDetails of the failures:")
        for name, exc, tb in failures:
            print(f"\n--- {name} ---")
            print(f"{type(exc).__name__}: {exc}")
            print(tb)
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
