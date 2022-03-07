import platform as pl

perfil_so = (
    "architecture",
    "linux_distribution",
    "mac_ver",
    'machine',
    "node",
    "platform",
    "processaor",
    "python_build",
    "python_compiler",
    "python_version",
    "release",
    "system",
    "uname",
    "version",

)

for perfil in perfil_so:
    if hasattr(pl, perfil):
        print('%s: %s' % (perfil, getattr(pl, perfil)()))
