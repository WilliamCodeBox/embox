[![](https://tokei.rs/b1/github/XAMPPRocky/tokei)](https://github.com/WilliamCodeBox/embox)

[![star this repo](http://githubbadges.com/star.svg?user=boennemann&repo=badges&style=flat)](https://github.com/WilliamCodeBox/embox)
[![fork this repo](http://githubbadges.com/fork.svg?user=boennemann&repo=badges&style=flat)](https://github.com/WilliamCodeBox/embox)

# embox

Fundamentals of Electromagnetic with Python

## Install

```bash
> pip search embox
> pip install embox
```

## Developer

### Testing

`embox` is tested by using the `pytest`[https://pypi.org/project/pytest/] package, and the test coverage is checked by using the `coverage`[https://pypi.org/project/coverage/] package.

A `.coveragerc` config file is created and located in the `embox` package root dir. This config file stores the sub commands `run` and `report` of `coverage`.

Run the following command to test coverage

```bash
coverage run -m pytest
```

Run the following command to show the test coverage report

```bash
coverage report
```
