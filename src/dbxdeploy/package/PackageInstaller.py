import re

class PackageInstaller:

    def __init__(
        self,
        packageBaseDir: str,
    ):
        self.__packageBaseDir = packageBaseDir

    def getPackageInstallCommand(self, packageFilePath: str):
        return 'dbutils.library.install(\'{}\')'.format(packageFilePath)

    def isPackageInstallCommand(self, commandCode: str):
        regExp = (
            '^' + re.escape('dbutils.library.install(\'' + self.__packageBaseDir) +
            '/[^/]+/[\\d]{4}-[\\d]{2}-[\\d]{2}_[\\d]{2}-[\\d]{2}-[\\d]{2}_[\\w]+/[^-]+-[\\d.]+-py3-none-any.whl\'\\)$'
        )

        return re.match(regExp, commandCode) is not None
