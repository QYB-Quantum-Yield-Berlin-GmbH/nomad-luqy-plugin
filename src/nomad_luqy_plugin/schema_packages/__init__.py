from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class LuQYSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_luqy_plugin.schema_packages.schema_package import m_package

        return m_package


schema_package_entry_point = LuQYSchemaPackageEntryPoint(
    name='LuQY Pro schema package',
    description='Schema package for LuQY Pro absolute PL.',
)
