# -*- mode: python ; coding: utf-8 -*-
VERSION = '0.29.0'
included_files = [
    ("build/Mtcli.ex5", "."),
    ("build/MA_TXT.ex5", "."),
    ("docs/README.md", "."),
    ("LICENSE", ".")
]
a = Analysis(
    ['mtcli\\mt.py'],
    pathex=[],
    binaries=[],
    datas=included_files,
    hiddenimports=['numpy'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='mt',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='mtcli-'+VERSION,
)
