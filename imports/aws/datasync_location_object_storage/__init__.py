r'''
# `aws_datasync_location_object_storage`

Refer to the Terraform Registry for docs: [`aws_datasync_location_object_storage`](https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage).
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class DatasyncLocationObjectStorage(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datasyncLocationObjectStorage.DatasyncLocationObjectStorage",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage aws_datasync_location_object_storage}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        agent_arns: typing.Sequence[builtins.str],
        bucket_name: builtins.str,
        server_hostname: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        server_certificate: typing.Optional[builtins.str] = None,
        server_port: typing.Optional[jsii.Number] = None,
        server_protocol: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage aws_datasync_location_object_storage} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param agent_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#agent_arns DatasyncLocationObjectStorage#agent_arns}.
        :param bucket_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#bucket_name DatasyncLocationObjectStorage#bucket_name}.
        :param server_hostname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#server_hostname DatasyncLocationObjectStorage#server_hostname}.
        :param access_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#access_key DatasyncLocationObjectStorage#access_key}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#id DatasyncLocationObjectStorage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param secret_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#secret_key DatasyncLocationObjectStorage#secret_key}.
        :param server_certificate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#server_certificate DatasyncLocationObjectStorage#server_certificate}.
        :param server_port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#server_port DatasyncLocationObjectStorage#server_port}.
        :param server_protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#server_protocol DatasyncLocationObjectStorage#server_protocol}.
        :param subdirectory: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#subdirectory DatasyncLocationObjectStorage#subdirectory}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#tags DatasyncLocationObjectStorage#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#tags_all DatasyncLocationObjectStorage#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7cbbb3866a69962dfba6ab89cccbe703a9348d2ff5ba97bb4b6e7643323099b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatasyncLocationObjectStorageConfig(
            agent_arns=agent_arns,
            bucket_name=bucket_name,
            server_hostname=server_hostname,
            access_key=access_key,
            id=id,
            secret_key=secret_key,
            server_certificate=server_certificate,
            server_port=server_port,
            server_protocol=server_protocol,
            subdirectory=subdirectory,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a DatasyncLocationObjectStorage resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DatasyncLocationObjectStorage to import.
        :param import_from_id: The id of the existing DatasyncLocationObjectStorage that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DatasyncLocationObjectStorage to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82c530ddde94280ab1c7f37d41b41080133c2903edf4067ff6e0a79586ba36b8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAccessKey")
    def reset_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessKey", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSecretKey")
    def reset_secret_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretKey", []))

    @jsii.member(jsii_name="resetServerCertificate")
    def reset_server_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerCertificate", []))

    @jsii.member(jsii_name="resetServerPort")
    def reset_server_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerPort", []))

    @jsii.member(jsii_name="resetServerProtocol")
    def reset_server_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerProtocol", []))

    @jsii.member(jsii_name="resetSubdirectory")
    def reset_subdirectory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubdirectory", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="agentArnsInput")
    def agent_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "agentArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="secretKeyInput")
    def secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="serverCertificateInput")
    def server_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="serverHostnameInput")
    def server_hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="serverPortInput")
    def server_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "serverPortInput"))

    @builtins.property
    @jsii.member(jsii_name="serverProtocolInput")
    def server_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="subdirectoryInput")
    def subdirectory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7432868caf6b7ac10ef892138c5077d6afb897c14937474ecca585c9929581f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="agentArns")
    def agent_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "agentArns"))

    @agent_arns.setter
    def agent_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d5a0097d30a66320610a71c055f4de0f2bab5bc3e6849580da96241d4ddc6f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b91ff8bae6bdfc17e17a72eef474184eef61a4e663603bc82a946e6db4e1cba0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f968af9e13cedbfacdb07646a60401eced7f3777547ae0611244c5de4aece4e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42da59f7f33d67465fe31f1dbe9aec035746b7b6121c3fcda35455e519dc1341)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverCertificate")
    def server_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverCertificate"))

    @server_certificate.setter
    def server_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9a870c404bb120fea295055ee4a903878ebcfa0d250db8dee54dd3126bc6b94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverCertificate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverHostname")
    def server_hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverHostname"))

    @server_hostname.setter
    def server_hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__519d6cea40abe07f8e8e930f6329e97610e2727f76dff55b5af3b8ab891f1dfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverHostname", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverPort")
    def server_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "serverPort"))

    @server_port.setter
    def server_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0563661154cba3501feb3c39eab4aec1d2ec0d4c664ccef0da1940f8cad05b6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverPort", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverProtocol")
    def server_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverProtocol"))

    @server_protocol.setter
    def server_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6b0005d29724cfab87c003ead4c99393bcc11b8e958fea3c8d7814a68dac12c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverProtocol", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb674c4c6a8836950af9c3d1b4042f6ad54a1d2a2f1820dd6e5dbf1520f3b444)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__419fdcaa997222c1d8701c4a76a0f549d6164cf62f329fd4ae54e2e06e7461df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__001631e2afec1c3f7f217a98b45f32461a2776a0f9a13cb27ab28a5d50f6fba5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.datasyncLocationObjectStorage.DatasyncLocationObjectStorageConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "agent_arns": "agentArns",
        "bucket_name": "bucketName",
        "server_hostname": "serverHostname",
        "access_key": "accessKey",
        "id": "id",
        "secret_key": "secretKey",
        "server_certificate": "serverCertificate",
        "server_port": "serverPort",
        "server_protocol": "serverProtocol",
        "subdirectory": "subdirectory",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class DatasyncLocationObjectStorageConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        agent_arns: typing.Sequence[builtins.str],
        bucket_name: builtins.str,
        server_hostname: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        server_certificate: typing.Optional[builtins.str] = None,
        server_port: typing.Optional[jsii.Number] = None,
        server_protocol: typing.Optional[builtins.str] = None,
        subdirectory: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param agent_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#agent_arns DatasyncLocationObjectStorage#agent_arns}.
        :param bucket_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#bucket_name DatasyncLocationObjectStorage#bucket_name}.
        :param server_hostname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#server_hostname DatasyncLocationObjectStorage#server_hostname}.
        :param access_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#access_key DatasyncLocationObjectStorage#access_key}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#id DatasyncLocationObjectStorage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param secret_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#secret_key DatasyncLocationObjectStorage#secret_key}.
        :param server_certificate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#server_certificate DatasyncLocationObjectStorage#server_certificate}.
        :param server_port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#server_port DatasyncLocationObjectStorage#server_port}.
        :param server_protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#server_protocol DatasyncLocationObjectStorage#server_protocol}.
        :param subdirectory: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#subdirectory DatasyncLocationObjectStorage#subdirectory}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#tags DatasyncLocationObjectStorage#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#tags_all DatasyncLocationObjectStorage#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62d805cf98e8627309a0d6d95bdc9a34936c7153c0f603da3235f8f5cf0d0d13)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument agent_arns", value=agent_arns, expected_type=type_hints["agent_arns"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument server_hostname", value=server_hostname, expected_type=type_hints["server_hostname"])
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
            check_type(argname="argument server_certificate", value=server_certificate, expected_type=type_hints["server_certificate"])
            check_type(argname="argument server_port", value=server_port, expected_type=type_hints["server_port"])
            check_type(argname="argument server_protocol", value=server_protocol, expected_type=type_hints["server_protocol"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_arns": agent_arns,
            "bucket_name": bucket_name,
            "server_hostname": server_hostname,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if access_key is not None:
            self._values["access_key"] = access_key
        if id is not None:
            self._values["id"] = id
        if secret_key is not None:
            self._values["secret_key"] = secret_key
        if server_certificate is not None:
            self._values["server_certificate"] = server_certificate
        if server_port is not None:
            self._values["server_port"] = server_port
        if server_protocol is not None:
            self._values["server_protocol"] = server_protocol
        if subdirectory is not None:
            self._values["subdirectory"] = subdirectory
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def agent_arns(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#agent_arns DatasyncLocationObjectStorage#agent_arns}.'''
        result = self._values.get("agent_arns")
        assert result is not None, "Required property 'agent_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#bucket_name DatasyncLocationObjectStorage#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_hostname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#server_hostname DatasyncLocationObjectStorage#server_hostname}.'''
        result = self._values.get("server_hostname")
        assert result is not None, "Required property 'server_hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#access_key DatasyncLocationObjectStorage#access_key}.'''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#id DatasyncLocationObjectStorage#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#secret_key DatasyncLocationObjectStorage#secret_key}.'''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#server_certificate DatasyncLocationObjectStorage#server_certificate}.'''
        result = self._values.get("server_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#server_port DatasyncLocationObjectStorage#server_port}.'''
        result = self._values.get("server_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def server_protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#server_protocol DatasyncLocationObjectStorage#server_protocol}.'''
        result = self._values.get("server_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdirectory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#subdirectory DatasyncLocationObjectStorage#subdirectory}.'''
        result = self._values.get("subdirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#tags DatasyncLocationObjectStorage#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/datasync_location_object_storage#tags_all DatasyncLocationObjectStorage#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatasyncLocationObjectStorageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DatasyncLocationObjectStorage",
    "DatasyncLocationObjectStorageConfig",
]

publication.publish()

def _typecheckingstub__b7cbbb3866a69962dfba6ab89cccbe703a9348d2ff5ba97bb4b6e7643323099b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    agent_arns: typing.Sequence[builtins.str],
    bucket_name: builtins.str,
    server_hostname: builtins.str,
    access_key: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    secret_key: typing.Optional[builtins.str] = None,
    server_certificate: typing.Optional[builtins.str] = None,
    server_port: typing.Optional[jsii.Number] = None,
    server_protocol: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82c530ddde94280ab1c7f37d41b41080133c2903edf4067ff6e0a79586ba36b8(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7432868caf6b7ac10ef892138c5077d6afb897c14937474ecca585c9929581f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5a0097d30a66320610a71c055f4de0f2bab5bc3e6849580da96241d4ddc6f4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b91ff8bae6bdfc17e17a72eef474184eef61a4e663603bc82a946e6db4e1cba0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f968af9e13cedbfacdb07646a60401eced7f3777547ae0611244c5de4aece4e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42da59f7f33d67465fe31f1dbe9aec035746b7b6121c3fcda35455e519dc1341(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9a870c404bb120fea295055ee4a903878ebcfa0d250db8dee54dd3126bc6b94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__519d6cea40abe07f8e8e930f6329e97610e2727f76dff55b5af3b8ab891f1dfd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0563661154cba3501feb3c39eab4aec1d2ec0d4c664ccef0da1940f8cad05b6a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6b0005d29724cfab87c003ead4c99393bcc11b8e958fea3c8d7814a68dac12c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb674c4c6a8836950af9c3d1b4042f6ad54a1d2a2f1820dd6e5dbf1520f3b444(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__419fdcaa997222c1d8701c4a76a0f549d6164cf62f329fd4ae54e2e06e7461df(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__001631e2afec1c3f7f217a98b45f32461a2776a0f9a13cb27ab28a5d50f6fba5(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62d805cf98e8627309a0d6d95bdc9a34936c7153c0f603da3235f8f5cf0d0d13(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    agent_arns: typing.Sequence[builtins.str],
    bucket_name: builtins.str,
    server_hostname: builtins.str,
    access_key: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    secret_key: typing.Optional[builtins.str] = None,
    server_certificate: typing.Optional[builtins.str] = None,
    server_port: typing.Optional[jsii.Number] = None,
    server_protocol: typing.Optional[builtins.str] = None,
    subdirectory: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
