# FLOCX Provider Design

The FLOCX provider is an OpenStack service that provides two key functions:

* It allows hardware owners to create offers for the FLOCX marketplace.
* It receives contracts from the FLOCX matcher and is responsible for fulfilling them.

## Architecture

**DIAGRAM TO COME**

## Data Model

### offers

An offer represents an agreement by a hardware owner to make their resource available for lease in the marketplace.

* *uuid*
* *resource_type*: This, combined with *resource_uuid*, defines the offered resource. It will typically be set to *ironic_node*.
* *resource_uuid*: This, combined with *resource_type*, defines the offered resource.
* *start_date*: The start date of the offer.
* *end_date*: The end date of the offer.
* *status*: Possible values are *open*, *claimed*, and *expired*.
* *properties*: This defines additional properties relevant to the offer which are not intrinsic the the resource itself (intrinsic properties are fetched from services like Ironic and passed onwards). One example is *price*.
* *created_at*
* *updated_at*

### contracts

A contract represents an agreement by the provider to make a resource available for use by a specified project.

* *uuid*
* *offer_uuid*: The offer to which the contract corresponds.
* *start_date*: The start date of the contract.
* *end_date*: The end date of the contract.
* *project_uuid*: The UUID of the OpenStack project to which the resource will be contracted.
* *status*: Possible values are *open*, *fulfilled*, and *expired*.
* *properties*: This defines additional properties relevant to the contract which are not intrinsic to the resource itself. One example is *contract_callback_url*.
* *created_at*
* *updated_at*

## REST API

**LINK OUT?**

## Manager

The FLOCX provider manager coordinates required actions triggered when the start dates and end dates of *offers* and *contracts* are reached. Actions include:

* When the *end_date* of an *offer* is reached, tell the FLOCX marketplace to remove the related resource from the marketplace.
* When the *start_date* of a *contract* is reached, set the appropriate property on the related resource to allow usage by the specified project.
* When the *end_date* of a *contract* is reached, remove all workloads from the related resource and unset the appropriate property on the related resource to prevent further usage by the specified project.