<!--- Copyright (C) from 2022 The Play Framework Contributors <https://github.com/playframework>, 2011-2021 Lightbend Inc. <https://www.lightbend.com> -->

# Contributor guidelines

## Reporting issues

If you wish to report an issue for Play Framework, please ensure you have done the following things:

* If it is a documentation issue with a simple fix, don't raise an issue, just edit the documentation yourself directly in GitHub and submit a pull request.  This will be quicker for you and everybody.
* If you are not 100% sure that it is a bug, then ask about it in the [Play Framework Forum](https://github.com/playframework/playframework/discussions) first.  You will get a lot more help a lot quicker in the forum if you raise it there.  The issue tracker is for verified bugs, not for questions.
* If you have a feature request, please raise it in the [GitHub Discussion forum](https://github.com/playframework/playframework/discussions) first.  The forum is the best place to discuss new features, and it may be that Play already provides something to achieve what you want to achieve and you didn't realise.
* If you are sure you have found a bug, then raise an issue.  Please be as specific as possible, including sample code that reproduces the problem, stack traces if there are any exceptions thrown, and versions of Play, OS, Java, etc.

When the above guidelines are not followed, a Play integrator may close the issue, directing you to the appropriate forum for further discussion.

## Contributing changes

### Prerequisites

Before making a contribution, it is important to make sure that the change you wish to make and the approach you wish to take will likely be accepted, otherwise you may end up doing a lot of work for nothing.  If the change is only small, for example, if it's a documentation change or a simple bugfix, then it's likely to be accepted with no prior discussion.  However, new features, or bigger refactorings should first be discussed in the [Play Framework Forum](https://github.com/playframework/playframework/discussions).

### Procedure

<!--- 1. Make sure you have signed the [XXX CLA](https://www.example.com/contribute/cla); if not, sign it online. -->
1. Ensure that your contribution meets the following guidelines:
    1. Live up to the current code standard:
        - Not violate [DRY](https://www.oreilly.com/library/view/97-things-every/9780596809515/ch30.html).
        - [Boy Scout Rule](https://www.oreilly.com/library/view/97-things-every/9780596809515/ch08.html) needs to have been applied.
    1. Regardless of whether the code introduces new features or fixes bugs or regressions, it must have comprehensive tests.  This includes when modifying existing code that isn't tested.
    1. Each API change must have the corresponding documentation change. The code must be well documented in the project's standard documentation format:
        * For Play in general see its [documentation guidelines](https://playframework.com/documentation/latest/Documentation).
        * For [Anorm](https://github.com/playframework/anorm) see [its documentation](https://playframework.com/documentation/latest/ScalaAnorm).
        * For [Play SOAP](https://playframework.github.io/play-soap/2.x/) see [its documentation](https://playframework.github.io/play-soap/2.x/).
    1. Implementation-wise, the following things should be avoided as much as possible:
        * Global state
        * Public mutable state
        * Implicit conversions
        * ThreadLocal
        * Locks
        * Casting
        * Introducing new, heavy external dependencies
    1. The Play API design rules are the following:
        * Play is a Java and Scala framework, make sure any changes have feature parity in both the Scala and Java APIs.
          * Java APIs should go to `.../src/main/java`, package structure is `play.myapipackage.xxxx`
          * Scala APIs should go to `.../src/main/scala`, where the package structure is `play.api.myapipackage`
          * However, this does not apply for all projects within the Play Framework GitHub organization, since some only support one of both APIs.
        * Features are forever, always think about whether a new feature really belongs to the core framework or if it should be implemented as a module
        * Code must conform to standard style guidelines and pass all tests (see [Run tests](https://www.playframework.com/documentation/latest/BuildingFromSource#Run-tests))
    1. New files must:
        * Have a copyright header in the style of
          ```
          Copyright (C) from 2022 The Play Framework Contributors <https://github.com/playframework>, 2011-2021 Lightbend Inc. <https://www.lightbend.com>
          ````
          followed by an empty line.
        * Not use `@author` tags since it does not encourage [Collective Code Ownership](https://www.extremeprogramming.org/rules/collective.html).
        * Usually a repository provides the sbt commands `validateCode` and `formatCode`. Run `sbt validateCode` to ensure all files are formatted and have the copyright header. If you changed docs, please run that command inside the `documentation` folder as well. If validation fails, you can run the `sbt formatCode` command to run all of the various formatters. If the commands are not available you are welcome to open a pull request to add them.
1. Ensure that your commits are squashed.  See [working with git](https://playframework.com/documentation/latest/WorkingWithGit) for more information.
1. Submit a pull request.

If the pull request does not meet the above requirements then the code should **not** be merged into main, or even reviewed - regardless of how good or important it is. No exceptions.

The pull request will be reviewed according to the [implementation decision process](https://playframework.com/community-process#Implementation-decisions).

## Backporting policy

Generally, all bug fixes, improvements and new features will go to the main branch.  Backports and other commits to stable branches will only be accepted if they meet the following conditions:

* The change only affects the documentation
* The change fixes a regression that was introduced in a previous stable release from that branch
* The change fixes a bug that impacts significant number of members of the open source community with no simple work arounds available
* Any other reason the Play steering committee deems appropriate

All backports and other commits to stable branches, in addition to satisfying the regular contributor guidelines, must also be binary and source compatible with previous releases on that branch.  The only exception to this is if a serious bug is impossible to fix without breaking the API, for example, a particular feature is not possible to use due to flaws in the API.
