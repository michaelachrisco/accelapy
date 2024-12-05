from .authentication_client import Client as AuthenticationClient
from .create_get_headers import CreateGetHeaders
from .payload import Payload
from .records_client import Client as RecordsClient
from .records_client.api.records import (
    v4_get_records,
    v4_post_records,
    v_4_get_records_record_id_additional,
    v4_get_records_ids,
    v4_delete_records_ids,
    v4_put_records_id,
    v4_get_records_mine,
    v_4_post_records_record_id_finalize,
    v_4_get_records_record_id_related,
    v_4_post_records_record_id_related,
    v_4_put_records_record_id_additional,
    v_4_delete_records_record_id_related_child_record_ids,
    v4_get_records_describe_create
)
from .records_client.api.records_activities import v_4_put_records_record_id_activities_id, v_4_post_records_record_id_activities, v_4_get_records_record_id_activities
from .records_client.api.records_addresses import v_4_post_records_record_id_addresses, v_4_delete_records_record_id_addresses_ids, v_4_put_records_record_id_addresses_id, v_4_get_records_record_id_addresses
from .records_client.api.records_addresses_custom_forms import v_4_get_records_record_id_addresses_address_id_custom_forms, v_4_get_records_record_id_addresses_address_id_custom_forms_meta

from .records_client.api.records_assets import v_4_post_records_record_id_assets, v_4_delete_records_record_id_assets_ids, v_4_get_records_record_id_assets
from .records_client.api.records_comments import v_4_put_records_record_id_comments_id, v_4_delete_records_record_id_comments_ids, v_4_post_records_record_id_comments, v_4_get_records_record_id_comments
from .records_client.api.records_condition_approvals import v_4_post_records_record_id_condition_approvals, v_4_delete_records_record_id_condition_approvals_ids, v_4_put_records_record_id_condition_approvals_id, v_4_get_records_record_id_condition_approvals, v_4_get_records_record_id_condition_approvals_id
from .records_client.api.records_conditions import v_4_put_records_record_id_conditions_id, v_4_delete_records_record_id_conditions_ids, v_4_post_records_record_id_conditions, v_4_get_records_record_id_conditions_id, v_4_get_records_record_id_conditions_id_histories, v_4_get_records_record_id_conditions
from .records_client.api.records_contacts import v_4_get_records_record_id_contacts_contact_id_addresses, v_4_delete_records_record_id_contacts_ids, v_4_post_records_record_id_contacts, v_4_put_records_record_id_contacts_id, v_4_delete_records_record_id_contacts_contact_id_addresses_ids, v_4_get_records_record_id_contacts, v_4_put_records_record_id_contacts_contact_id_addresses_id, v_4_post_records_record_id_contacts_contact_id_addresses
from .records_client.api.records_contacts_custom_forms import v_4_get_records_record_id_contacts_contact_id_custom_forms, v_4_get_records_record_id_contacts_contact_id_custom_forms_form_id_meta, v_4_put_records_record_id_contacts_contact_id_custom_forms, v_4_get_records_record_id_contacts_contact_id_custom_forms_meta
from .records_client.api.records_contacts_custom_tables import v_4_get_records_record_id_contacts_contact_id_custom_tables, v_4_get_records_record_id_contacts_contact_id_custom_tables_table_id_meta, v_4_put_records_record_id_contacts_contact_id_custom_tables, v_4_get_records_record_id_contacts_contact_id_custom_tables_meta
from .records_client.api.records_costs import v_4_put_records_record_id_costs_id, v_4_delete_records_record_id_costs_ids, v_4_get_records_record_id_costs
from .records_client.api.records_custom_forms import v_4_put_records_record_id_custom_forms, v_4_get_records_record_id_custom_forms, v_4_get_records_record_id_custom_forms_meta, v_4_get_records_record_id_custom_forms_form_id_meta
from .records_client.api.records_custom_tables import v_4_put_records_record_id_custom_tables, v_4_get_records_record_id_custom_tables, v_4_get_records_record_id_custom_tables_meta, v_4_get_records_record_id_custom_tables_table_id_meta, v_4_get_records_record_id_custom_tables_table_id
from .records_client.api.records_documents import v_4_delete_records_record_id_documents_document_ids, v_4_post_records_record_id_documents, v_4_get_records_record_id_document_categories, v_4_get_records_record_id_documents
from .records_client.api.records_fees import v_4_post_records_record_id_fees, v_4_put_records_record_id_fees_estimate, v_4_get_records_record_id_fees
from .records_client.api.records_inspections import v_4_get_records_record_id_inspections, v_4_get_records_record_ids_inspection_types
from .records_client.api.records_invoices import v_4_post_records_record_id_invoices, v_4_get_records_record_id_invoices
from .records_client.api.records_owners import v_4_put_records_record_id_owners_id, v_4_delete_records_record_id_owners_ids, v_4_post_records_record_id_owners, v_4_get_records_record_id_owners
from .records_client.api.records_parcels import v_4_put_records_record_id_parcels_id, v_4_delete_records_record_id_parcels_ids, v_4_post_records_record_id_parcels, v_4_get_records_record_id_parcels
from .records_client.api.records_part_transactions import v_4_post_records_record_id_part_transaction, v_4_delete_records_record_id_part_transaction_ids, v_4_get_records_record_id_part_transaction
from .records_client.api.records_payments import v_4_get_records_record_id_payments_payment_id, v_4_get_records_record_id_payments
from .records_client.api.records_professionals import v_4_put_records_record_id_professionals_id, v_4_delete_records_record_id_professionals_ids, v_4_post_records_record_id_professionals, v_4_get_records_record_id_professionals
from .records_client.api.records_trust_accounts import v_4_get_records_record_id_trust_accounts
from .records_client.api.records_votes import v_4_get_records_record_id_votes_summary, v_4_post_records_record_id_votes, v_4_get_records_record_id_votes
from .records_client.api.records_workflows import v_4_get_records_record_id_workflow_tasks, v_4_get_records_record_id_workflow_tasks_comments_histories, v_4_get_records_record_id_workflow_tasks_task_id_custom_forms, v_4_get_records_record_id_workflow_tasks_id_statuses, v_4_put_records_record_id_workflow_tasks_id, v_4_get_records_record_id_workflow_tasks_task_id_custom_forms_meta, v_4_get_records_record_id_workflow_tasks_id, v_4_get_records_record_id_workflow_tasks_histories, v_4_put_records_record_id_workflow_tasks_task_id_custom_forms

class AccelaClient:
    def __init__(self,
                 payload: Payload,
                 url='https://apis.accela.com/'):
        self.url = url
        self.payload = payload
        self.create_get_headers = CreateGetHeaders(payload.to_payload_str())
        self._authentication_client = AuthenticationClient(base_url=url)
        self._records_client = RecordsClient(base_url=url)
        self.v4_get_records = v4_get_records
        self.v4_post_records = v4_post_records
        self.v_4_get_records_record_id_additional = v_4_get_records_record_id_additional
        self.v4_get_records_ids = v4_get_records_ids
        self.v4_delete_records_ids = v4_delete_records_ids
        self.v4_put_records_id = v4_put_records_id
        self.v4_get_records_mine = v4_get_records_mine
        self.v_4_post_records_record_id_finalize = v_4_post_records_record_id_finalize
        self.v_4_get_records_record_id_related = v_4_get_records_record_id_related
        self.v_4_post_records_record_id_related = v_4_post_records_record_id_related
        self.v_4_put_records_record_id_additional = v_4_put_records_record_id_additional
        self.v_4_delete_records_record_id_related_child_record_ids = v_4_delete_records_record_id_related_child_record_ids
        self.v4_get_records_describe_create = v4_get_records_describe_create

        self.v_4_put_records_record_id_activities_id = v_4_put_records_record_id_activities_id
        self.v_4_post_records_record_id_activities = v_4_post_records_record_id_activities
        self.v_4_get_records_record_id_activities = v_4_get_records_record_id_activities

        self.v_4_post_records_record_id_addresses = v_4_post_records_record_id_addresses
        self.v_4_delete_records_record_id_addresses_ids = v_4_delete_records_record_id_addresses_ids
        self.v_4_put_records_record_id_addresses_id = v_4_put_records_record_id_addresses_id
        self.v_4_get_records_record_id_addresses = v_4_get_records_record_id_addresses

        self.v_4_get_records_record_id_addresses_address_id_custom_forms = v_4_get_records_record_id_addresses_address_id_custom_forms
        self.v_4_get_records_record_id_addresses_address_id_custom_forms_meta = v_4_get_records_record_id_addresses_address_id_custom_forms_meta

        self.v_4_post_records_record_id_assets = v_4_post_records_record_id_assets
        self.v_4_delete_records_record_id_assets_ids = v_4_delete_records_record_id_assets_ids
        self.v_4_get_records_record_id_assets = v_4_get_records_record_id_assets

        self.v_4_put_records_record_id_comments_id = v_4_put_records_record_id_comments_id
        self.v_4_delete_records_record_id_comments_ids = v_4_delete_records_record_id_comments_ids
        self.v_4_post_records_record_id_comments = v_4_post_records_record_id_comments
        self.v_4_get_records_record_id_comments = v_4_get_records_record_id_comments

        self.v_4_post_records_record_id_condition_approvals = v_4_post_records_record_id_condition_approvals
        self.v_4_delete_records_record_id_condition_approvals_ids = v_4_delete_records_record_id_condition_approvals_ids
        self.v_4_put_records_record_id_condition_approvals_id = v_4_put_records_record_id_condition_approvals_id
        self.v_4_get_records_record_id_condition_approvals = v_4_get_records_record_id_condition_approvals
        self.v_4_get_records_record_id_condition_approvals_id = v_4_get_records_record_id_condition_approvals_id

        self.v_4_put_records_record_id_conditions_id = v_4_put_records_record_id_conditions_id
        self.v_4_delete_records_record_id_conditions_ids = v_4_delete_records_record_id_conditions_ids
        self.v_4_post_records_record_id_conditions = v_4_post_records_record_id_conditions
        self.v_4_get_records_record_id_conditions_id = v_4_get_records_record_id_conditions_id
        self.v_4_get_records_record_id_conditions_id_histories = v_4_get_records_record_id_conditions_id_histories
        self.v_4_get_records_record_id_conditions = v_4_get_records_record_id_conditions

        self.v_4_get_records_record_id_contacts_contact_id_addresses = v_4_get_records_record_id_contacts_contact_id_addresses
        self.v_4_delete_records_record_id_contacts_ids = v_4_delete_records_record_id_contacts_ids
        self.v_4_post_records_record_id_contacts = v_4_post_records_record_id_contacts
        self.v_4_put_records_record_id_contacts_id = v_4_put_records_record_id_contacts_id
        self.v_4_delete_records_record_id_contacts_contact_id_addresses_ids = v_4_delete_records_record_id_contacts_contact_id_addresses_ids
        self.v_4_get_records_record_id_contacts = v_4_get_records_record_id_contacts
        self.v_4_put_records_record_id_contacts_contact_id_addresses_id = v_4_put_records_record_id_contacts_contact_id_addresses_id
        self.v_4_post_records_record_id_contacts_contact_id_addresses = v_4_post_records_record_id_contacts_contact_id_addresses

        self.v_4_get_records_record_id_contacts_contact_id_custom_forms = v_4_get_records_record_id_contacts_contact_id_custom_forms
        self.v_4_get_records_record_id_contacts_contact_id_custom_forms_form_id_meta = v_4_get_records_record_id_contacts_contact_id_custom_forms_form_id_meta
        self.v_4_put_records_record_id_contacts_contact_id_custom_forms = v_4_put_records_record_id_contacts_contact_id_custom_forms
        self.v_4_get_records_record_id_contacts_contact_id_custom_forms_meta = v_4_get_records_record_id_contacts_contact_id_custom_forms_meta

        self.v_4_get_records_record_id_contacts_contact_id_custom_tables = v_4_get_records_record_id_contacts_contact_id_custom_tables
        self.v_4_get_records_record_id_contacts_contact_id_custom_tables_table_id_meta = v_4_get_records_record_id_contacts_contact_id_custom_tables_table_id_meta
        self.v_4_put_records_record_id_contacts_contact_id_custom_tables = v_4_put_records_record_id_contacts_contact_id_custom_tables
        self.v_4_get_records_record_id_contacts_contact_id_custom_tables_meta = v_4_get_records_record_id_contacts_contact_id_custom_tables_meta

        self.v_4_put_records_record_id_costs_id = v_4_put_records_record_id_costs_id
        self.v_4_delete_records_record_id_costs_ids = v_4_delete_records_record_id_costs_ids
        self.v_4_get_records_record_id_costs = v_4_get_records_record_id_costs

        self.v_4_put_records_record_id_custom_forms = v_4_put_records_record_id_custom_forms
        self.v_4_get_records_record_id_custom_forms = v_4_get_records_record_id_custom_forms
        self.v_4_get_records_record_id_custom_forms_meta = v_4_get_records_record_id_custom_forms_meta
        self.v_4_get_records_record_id_custom_forms_form_id_meta = v_4_get_records_record_id_custom_forms_form_id_meta

        self.v_4_put_records_record_id_custom_tables = v_4_put_records_record_id_custom_tables
        self.v_4_get_records_record_id_custom_tables = v_4_get_records_record_id_custom_tables
        self.v_4_get_records_record_id_custom_tables_meta = v_4_get_records_record_id_custom_tables_meta
        self.v_4_get_records_record_id_custom_tables_table_id_meta = v_4_get_records_record_id_custom_tables_table_id_meta
        self.v_4_get_records_record_id_custom_tables_table_id = v_4_get_records_record_id_custom_tables_table_id

        self.v_4_delete_records_record_id_documents_document_ids = v_4_delete_records_record_id_documents_document_ids
        self.v_4_post_records_record_id_documents = v_4_post_records_record_id_documents
        self.v_4_get_records_record_id_document_categories = v_4_get_records_record_id_document_categories
        self.v_4_get_records_record_id_documents = v_4_get_records_record_id_documents

        self.v_4_post_records_record_id_fees = v_4_post_records_record_id_fees
        self.v_4_put_records_record_id_fees_estimate = v_4_put_records_record_id_fees_estimate
        self.v_4_get_records_record_id_fees = v_4_get_records_record_id_fees

        self.v_4_get_records_record_id_inspections = v_4_get_records_record_id_inspections
        self.v_4_get_records_record_ids_inspection_types = v_4_get_records_record_ids_inspection_types

        self.v_4_post_records_record_id_invoices = v_4_post_records_record_id_invoices
        self.v_4_get_records_record_id_invoices = v_4_get_records_record_id_invoices


        self.v_4_put_records_record_id_owners_id = v_4_put_records_record_id_owners_id
        self.v_4_delete_records_record_id_owners_ids = v_4_delete_records_record_id_owners_ids
        self.v_4_post_records_record_id_owners = v_4_post_records_record_id_owners
        self.v_4_get_records_record_id_owners = v_4_get_records_record_id_owners

        self.v_4_put_records_record_id_parcels_id = v_4_put_records_record_id_parcels_id
        self.v_4_delete_records_record_id_parcels_ids = v_4_delete_records_record_id_parcels_ids
        self.v_4_post_records_record_id_parcels = v_4_post_records_record_id_parcels
        self.v_4_get_records_record_id_parcels = v_4_get_records_record_id_parcels

        self.v_4_post_records_record_id_part_transaction = v_4_post_records_record_id_part_transaction
        self.v_4_delete_records_record_id_part_transaction_ids = v_4_delete_records_record_id_part_transaction_ids
        self.v_4_get_records_record_id_part_transaction = v_4_get_records_record_id_part_transaction

        self.v_4_get_records_record_id_payments_payment_id = v_4_get_records_record_id_payments_payment_id
        self.v_4_get_records_record_id_payments = v_4_get_records_record_id_payments

        self.v_4_put_records_record_id_professionals_id = v_4_put_records_record_id_professionals_id
        self.v_4_delete_records_record_id_professionals_ids = v_4_delete_records_record_id_professionals_ids
        self.v_4_post_records_record_id_professionals = v_4_post_records_record_id_professionals
        self.v_4_get_records_record_id_professionals = v_4_get_records_record_id_professionals

        self.v_4_get_records_record_id_trust_accounts = v_4_get_records_record_id_trust_accounts

        self.v_4_get_records_record_id_votes_summary = v_4_get_records_record_id_votes_summary
        self.v_4_post_records_record_id_votes = v_4_post_records_record_id_votes
        self.v_4_get_records_record_id_votes = v_4_get_records_record_id_votes

        self.v_4_get_records_record_id_workflow_tasks = v_4_get_records_record_id_workflow_tasks
        self.v_4_get_records_record_id_workflow_tasks_comments_histories = v_4_get_records_record_id_workflow_tasks_comments_histories
        self.v_4_get_records_record_id_workflow_tasks_task_id_custom_forms = v_4_get_records_record_id_workflow_tasks_task_id_custom_forms
        self.v_4_get_records_record_id_workflow_tasks_id_statuses = v_4_get_records_record_id_workflow_tasks_id_statuses
        self.v_4_put_records_record_id_workflow_tasks_id = v_4_put_records_record_id_workflow_tasks_id
        self.v_4_get_records_record_id_workflow_tasks_task_id_custom_forms_meta = v_4_get_records_record_id_workflow_tasks_task_id_custom_forms_meta
        self.v_4_get_records_record_id_workflow_tasks_id = v_4_get_records_record_id_workflow_tasks_id
        self.v_4_get_records_record_id_workflow_tasks_histories = v_4_get_records_record_id_workflow_tasks_histories
        self.v_4_put_records_record_id_workflow_tasks_task_id_custom_forms = v_4_put_records_record_id_workflow_tasks_task_id_custom_forms


    @property
    def authentication_client(self):
        return self._authentication_client.with_headers(self.create_get_headers.get_header())

    @property
    def records_client(self):
        return self._records_client.with_headers(self.create_get_headers.get_header())
