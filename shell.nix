{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (ps: with ps; [
      altgraph
      beautifulsoup4
      gitpython
      numpy
      packaging
      pandas
      pefile
      pillow
      pyinstaller
      pyinstaller-hooks-contrib
      python-dateutil
      pytz
      six
      screeninfo
      tkinter
      tzdata
    ]))
  ];
}
