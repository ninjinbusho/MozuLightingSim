# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['mozulightingsim.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['tape', 'vulcbeat', 'drivers.rgb', 'drivers.rgb4', 'drivers.keybdsettings', 'drivers.minimirror', 'drivers.abdmxraw', 'drivers.primary', 'drivers.abdmxv2raw', 'drivers.picoraw'],
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
    a.binaries,
    a.datas,
    [],
    name='mozulightingsim',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
