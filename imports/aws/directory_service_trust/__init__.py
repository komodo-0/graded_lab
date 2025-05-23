r'''
# `aws_directory_service_trust`

Refer to the Terraform Registry for docs: [`aws_directory_service_trust`](https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust).
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


class DirectoryServiceTrust(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.directoryServiceTrust.DirectoryServiceTrust",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust aws_directory_service_trust}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        directory_id: builtins.str,
        remote_domain_name: builtins.str,
        trust_direction: builtins.str,
        trust_password: builtins.str,
        conditional_forwarder_ip_addrs: typing.Optional[typing.Sequence[builtins.str]] = None,
        delete_associated_conditional_forwarder: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        selective_auth: typing.Optional[builtins.str] = None,
        trust_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust aws_directory_service_trust} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param directory_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#directory_id DirectoryServiceTrust#directory_id}.
        :param remote_domain_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#remote_domain_name DirectoryServiceTrust#remote_domain_name}.
        :param trust_direction: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#trust_direction DirectoryServiceTrust#trust_direction}.
        :param trust_password: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#trust_password DirectoryServiceTrust#trust_password}.
        :param conditional_forwarder_ip_addrs: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#conditional_forwarder_ip_addrs DirectoryServiceTrust#conditional_forwarder_ip_addrs}.
        :param delete_associated_conditional_forwarder: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#delete_associated_conditional_forwarder DirectoryServiceTrust#delete_associated_conditional_forwarder}.
        :param selective_auth: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#selective_auth DirectoryServiceTrust#selective_auth}.
        :param trust_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#trust_type DirectoryServiceTrust#trust_type}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad936eb7be05421ba1de5e40b6d4e122c014b9a5f7a9bfaba49c5d12a98d46fd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DirectoryServiceTrustConfig(
            directory_id=directory_id,
            remote_domain_name=remote_domain_name,
            trust_direction=trust_direction,
            trust_password=trust_password,
            conditional_forwarder_ip_addrs=conditional_forwarder_ip_addrs,
            delete_associated_conditional_forwarder=delete_associated_conditional_forwarder,
            selective_auth=selective_auth,
            trust_type=trust_type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a DirectoryServiceTrust resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DirectoryServiceTrust to import.
        :param import_from_id: The id of the existing DirectoryServiceTrust that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DirectoryServiceTrust to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df2657171d9c146d37d606020f0f337d0e4ba316c1861c394ded653b4ece8c4d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetConditionalForwarderIpAddrs")
    def reset_conditional_forwarder_ip_addrs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionalForwarderIpAddrs", []))

    @jsii.member(jsii_name="resetDeleteAssociatedConditionalForwarder")
    def reset_delete_associated_conditional_forwarder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteAssociatedConditionalForwarder", []))

    @jsii.member(jsii_name="resetSelectiveAuth")
    def reset_selective_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelectiveAuth", []))

    @jsii.member(jsii_name="resetTrustType")
    def reset_trust_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustType", []))

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
    @jsii.member(jsii_name="createdDateTime")
    def created_date_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDateTime"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDateTime")
    def last_updated_date_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDateTime"))

    @builtins.property
    @jsii.member(jsii_name="stateLastUpdatedDateTime")
    def state_last_updated_date_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateLastUpdatedDateTime"))

    @builtins.property
    @jsii.member(jsii_name="trustState")
    def trust_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trustState"))

    @builtins.property
    @jsii.member(jsii_name="trustStateReason")
    def trust_state_reason(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trustStateReason"))

    @builtins.property
    @jsii.member(jsii_name="conditionalForwarderIpAddrsInput")
    def conditional_forwarder_ip_addrs_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "conditionalForwarderIpAddrsInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteAssociatedConditionalForwarderInput")
    def delete_associated_conditional_forwarder_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteAssociatedConditionalForwarderInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryIdInput")
    def directory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteDomainNameInput")
    def remote_domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteDomainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="selectiveAuthInput")
    def selective_auth_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectiveAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="trustDirectionInput")
    def trust_direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trustDirectionInput"))

    @builtins.property
    @jsii.member(jsii_name="trustPasswordInput")
    def trust_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trustPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="trustTypeInput")
    def trust_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trustTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionalForwarderIpAddrs")
    def conditional_forwarder_ip_addrs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "conditionalForwarderIpAddrs"))

    @conditional_forwarder_ip_addrs.setter
    def conditional_forwarder_ip_addrs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56efaaa50535cd0df231a2c0cc1cf520967249f97c821db434848b3e9db0fd5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditionalForwarderIpAddrs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deleteAssociatedConditionalForwarder")
    def delete_associated_conditional_forwarder(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteAssociatedConditionalForwarder"))

    @delete_associated_conditional_forwarder.setter
    def delete_associated_conditional_forwarder(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61cab9c082cd77a7aa59f21b8be28c570ca7c612a34084ecde46c7851c1d4519)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAssociatedConditionalForwarder", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63439a9d8f04881d6f01834330b4c6709f7191a006fae35cfeff53cd2e984a5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="remoteDomainName")
    def remote_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteDomainName"))

    @remote_domain_name.setter
    def remote_domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87268ff03918dc9544dd8945207624d1d530b793f3d14061f12fe6d0028395f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteDomainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="selectiveAuth")
    def selective_auth(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selectiveAuth"))

    @selective_auth.setter
    def selective_auth(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e54e18519c426f1072422e5ffb7dcf8eb207c3c346b8a1ff36fda85867b62146)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectiveAuth", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="trustDirection")
    def trust_direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trustDirection"))

    @trust_direction.setter
    def trust_direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__068edbc3463ccc8eccd1a0b4ec4732788da600881ee9224d5ef90de70c6fba12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustDirection", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="trustPassword")
    def trust_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trustPassword"))

    @trust_password.setter
    def trust_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b348f5bded5d070c01fd404051bb91fe59678b436f628173978ad41ca385824c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustPassword", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="trustType")
    def trust_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trustType"))

    @trust_type.setter
    def trust_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__527da29283496e47b9c11dd69d917fb503a29472a66a102a937701597f71f13e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustType", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.directoryServiceTrust.DirectoryServiceTrustConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "directory_id": "directoryId",
        "remote_domain_name": "remoteDomainName",
        "trust_direction": "trustDirection",
        "trust_password": "trustPassword",
        "conditional_forwarder_ip_addrs": "conditionalForwarderIpAddrs",
        "delete_associated_conditional_forwarder": "deleteAssociatedConditionalForwarder",
        "selective_auth": "selectiveAuth",
        "trust_type": "trustType",
    },
)
class DirectoryServiceTrustConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        directory_id: builtins.str,
        remote_domain_name: builtins.str,
        trust_direction: builtins.str,
        trust_password: builtins.str,
        conditional_forwarder_ip_addrs: typing.Optional[typing.Sequence[builtins.str]] = None,
        delete_associated_conditional_forwarder: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        selective_auth: typing.Optional[builtins.str] = None,
        trust_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param directory_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#directory_id DirectoryServiceTrust#directory_id}.
        :param remote_domain_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#remote_domain_name DirectoryServiceTrust#remote_domain_name}.
        :param trust_direction: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#trust_direction DirectoryServiceTrust#trust_direction}.
        :param trust_password: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#trust_password DirectoryServiceTrust#trust_password}.
        :param conditional_forwarder_ip_addrs: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#conditional_forwarder_ip_addrs DirectoryServiceTrust#conditional_forwarder_ip_addrs}.
        :param delete_associated_conditional_forwarder: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#delete_associated_conditional_forwarder DirectoryServiceTrust#delete_associated_conditional_forwarder}.
        :param selective_auth: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#selective_auth DirectoryServiceTrust#selective_auth}.
        :param trust_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#trust_type DirectoryServiceTrust#trust_type}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18f3a2b2223f5b8e1956c1c0d1044e9239f75d10a8f7f9234a984d7541e8edb9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
            check_type(argname="argument remote_domain_name", value=remote_domain_name, expected_type=type_hints["remote_domain_name"])
            check_type(argname="argument trust_direction", value=trust_direction, expected_type=type_hints["trust_direction"])
            check_type(argname="argument trust_password", value=trust_password, expected_type=type_hints["trust_password"])
            check_type(argname="argument conditional_forwarder_ip_addrs", value=conditional_forwarder_ip_addrs, expected_type=type_hints["conditional_forwarder_ip_addrs"])
            check_type(argname="argument delete_associated_conditional_forwarder", value=delete_associated_conditional_forwarder, expected_type=type_hints["delete_associated_conditional_forwarder"])
            check_type(argname="argument selective_auth", value=selective_auth, expected_type=type_hints["selective_auth"])
            check_type(argname="argument trust_type", value=trust_type, expected_type=type_hints["trust_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "directory_id": directory_id,
            "remote_domain_name": remote_domain_name,
            "trust_direction": trust_direction,
            "trust_password": trust_password,
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
        if conditional_forwarder_ip_addrs is not None:
            self._values["conditional_forwarder_ip_addrs"] = conditional_forwarder_ip_addrs
        if delete_associated_conditional_forwarder is not None:
            self._values["delete_associated_conditional_forwarder"] = delete_associated_conditional_forwarder
        if selective_auth is not None:
            self._values["selective_auth"] = selective_auth
        if trust_type is not None:
            self._values["trust_type"] = trust_type

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
    def directory_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#directory_id DirectoryServiceTrust#directory_id}.'''
        result = self._values.get("directory_id")
        assert result is not None, "Required property 'directory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def remote_domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#remote_domain_name DirectoryServiceTrust#remote_domain_name}.'''
        result = self._values.get("remote_domain_name")
        assert result is not None, "Required property 'remote_domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trust_direction(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#trust_direction DirectoryServiceTrust#trust_direction}.'''
        result = self._values.get("trust_direction")
        assert result is not None, "Required property 'trust_direction' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trust_password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#trust_password DirectoryServiceTrust#trust_password}.'''
        result = self._values.get("trust_password")
        assert result is not None, "Required property 'trust_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conditional_forwarder_ip_addrs(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#conditional_forwarder_ip_addrs DirectoryServiceTrust#conditional_forwarder_ip_addrs}.'''
        result = self._values.get("conditional_forwarder_ip_addrs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def delete_associated_conditional_forwarder(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#delete_associated_conditional_forwarder DirectoryServiceTrust#delete_associated_conditional_forwarder}.'''
        result = self._values.get("delete_associated_conditional_forwarder")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def selective_auth(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#selective_auth DirectoryServiceTrust#selective_auth}.'''
        result = self._values.get("selective_auth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trust_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/4.67.0/docs/resources/directory_service_trust#trust_type DirectoryServiceTrust#trust_type}.'''
        result = self._values.get("trust_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DirectoryServiceTrustConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DirectoryServiceTrust",
    "DirectoryServiceTrustConfig",
]

publication.publish()

def _typecheckingstub__ad936eb7be05421ba1de5e40b6d4e122c014b9a5f7a9bfaba49c5d12a98d46fd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    directory_id: builtins.str,
    remote_domain_name: builtins.str,
    trust_direction: builtins.str,
    trust_password: builtins.str,
    conditional_forwarder_ip_addrs: typing.Optional[typing.Sequence[builtins.str]] = None,
    delete_associated_conditional_forwarder: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    selective_auth: typing.Optional[builtins.str] = None,
    trust_type: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__df2657171d9c146d37d606020f0f337d0e4ba316c1861c394ded653b4ece8c4d(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56efaaa50535cd0df231a2c0cc1cf520967249f97c821db434848b3e9db0fd5b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61cab9c082cd77a7aa59f21b8be28c570ca7c612a34084ecde46c7851c1d4519(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63439a9d8f04881d6f01834330b4c6709f7191a006fae35cfeff53cd2e984a5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87268ff03918dc9544dd8945207624d1d530b793f3d14061f12fe6d0028395f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e54e18519c426f1072422e5ffb7dcf8eb207c3c346b8a1ff36fda85867b62146(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__068edbc3463ccc8eccd1a0b4ec4732788da600881ee9224d5ef90de70c6fba12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b348f5bded5d070c01fd404051bb91fe59678b436f628173978ad41ca385824c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__527da29283496e47b9c11dd69d917fb503a29472a66a102a937701597f71f13e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18f3a2b2223f5b8e1956c1c0d1044e9239f75d10a8f7f9234a984d7541e8edb9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    directory_id: builtins.str,
    remote_domain_name: builtins.str,
    trust_direction: builtins.str,
    trust_password: builtins.str,
    conditional_forwarder_ip_addrs: typing.Optional[typing.Sequence[builtins.str]] = None,
    delete_associated_conditional_forwarder: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    selective_auth: typing.Optional[builtins.str] = None,
    trust_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
