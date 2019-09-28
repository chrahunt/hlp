import nox


@nox.session(python=["2.7", "3.7"])
def test(session):
    session.install("pytest")
    session.install(".")
    session.run("pytest", *session.posargs)


@nox.session
def lint(session):
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files", *session.posargs)


@nox.session
def build(session):
    session.install("pep517")
    session.run(
        "python",
        "-m",
        "pep517.build",
        "--source",
        "--binary",
        "--out-dir",
        "dist/",
        ".",
    )
