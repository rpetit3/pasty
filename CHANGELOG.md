# Releases

## v2.2.1 rpetit3/pasty "HB13" - 2024/08/25

- adjust default parameters for `--min-pident` and `--min-coverage` to 90 each

## v2.2.0 rpetit3/pasty "JBPA" - 2024/08/25

- add default parameters for `--min-pident` and `--min-coverage` in the YAML

## v2.1.0 rpetit3/pasty "LESB58" - 2024/08/19

- add serogroups O15 and O17 https://github.com/rpetit3/pasty/pull/5 @StefaanVerwimp
- update GHA tests with latest serogroups

## v2.0.2 rpetit3/pasty "19BR+1" - 2024/08/14

- no changes, fixing upstream bioconda install

## v2.0.1 rpetit3/pasty "19BR" - 2024/08/14

- updated for latest changes in camlhmp
- updated GHA workflow

## v2.0.0 rpetit3/pasty "PACS2" - 2024/07/22

- `pasty` now uses the `camlhmp` framework for classification
- fixed O2 and O5 serogroup classification

## v1.0.3 rpetit3/pasty "PAC1" - 2023/08/04

- fixed bug when int concatenated to str during blast
- print the usage when no options provided
- add `--check` to check for dependencies

## v1.0.2 rpetit3/pasty "PA7" - 2022/12/01

- improved coverage calculation
- added more comments

## v1.0.1 rpetit3/pasty "UCBPP-PA14" - 2022/11/30

- improved outputs messaging
- test data naming reflects expected serogroups
- added expected results from tests
- added gitpod support
- updated CI

## v1.0.0 rpetit3/pasty "PAO1" - 2022/07/20

- Initial release of pasty
