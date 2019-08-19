# FLOCX Setup

This document describes the steps necessary to install a functioning FLOCX
system. Read the [FLOCX Architecture document](architecture.md) for details on
how FLOCX works.

## OpenStack

FLOCX requires Keystone, Ironic, and Nova. Nova needs to be configured as
follows:

- [Configure the Compute service to use the Bare Metal service](https://docs.openstack.org/ironic/latest/install/configure-compute.html)
- [Use the Custom Nova Filter for ESI](https://github.com/CCI-MOC/esi-common/)

It is recommended that you prevent hardware owners from accessing the Ironic
API, as this would give them access to all baremetal nodes. Instead, we
recommend
[creating custom ESI Mistral Workflows](https://github.com/CCI-MOC/esi-common/).
These workflows mirror the Ironic API - only they first check that the hardware
owner has administrative access to a node.

## ESI Leap Provider

The ESI Leap Provider  is a FLOCX OpenStack service that is responsible for
allowing hardware owners to make offers; for retrieving contracts from the
marketplace; and for fulfilling those contracts.

- [Instructions](https://github.com/CCI-MOC/esi-leap)

## FLOCX Marketplace

The FLOCX Marketplace is responsible for receiving offers (from the Provider)
and bids (from consumers, through the API or UI). It then matches offers and
bids to create contracts for use by the Provider.

- [Instructions](https://github.com/CCI-MOC/flocx-market)

## FLOCX UI

The FLOCX UI is an optional component. It is a Horizon plugin.

- [Instructions](https://github.com/CCI-MOC/flocx-ui)
