CREATE TABLE suppliers (
    id INTEGER,
    legal_name text,
    trade_name text,
    country text,
    tax_id text,
    tax_id_type text,
    email text,
    phone INTEGER,
    contact_name text,
    is_active text,
    created_at text,
    updated_at text
);

CREATE TABLE goods_receipt_items (
    id INTEGER,
    goods_receipt_id INTEGER,
    purchase_order_item_id INTEGER,
    quantity_received text
);

CREATE TABLE purchase_orders (
    id INTEGER,
    po_number text,
    supplier_id INTEGER,
    buyer_id INTEGER,
    destination_location_id INTEGER,
    status text,
    currency text,
    subtotal text,
    total text,
    placed_at text,
    expected_delivery_at text,
    created_at text,
    updated_at text
);

CREATE TABLE stock_movements (
    id INTEGER,
    product_variant_id INTEGER,
    location_id INTEGER,
    movement_type text,
    quantity text,
    reference_table text,
    reference_id INTEGER,
    employee_id INTEGER,
    notes text,
    occurred_at text,
    created_at text
);

CREATE TABLE addresses (
    id INTEGER,
    customer_id INTEGER,
    address_type text,
    postal_code text,
    street text,
    number INTEGER,
    complement text,
    district text,
    city text,
    state text,
    country text,
    is_primary text
);

CREATE TABLE attributes (
    id INTEGER,
    name text,
    data_type text
);

CREATE TABLE locations (
    id INTEGER,
    name text,
    location_type text,
    postal_code text,
    street text,
    number INTEGER,
    complement text,
    district text,
    city text,
    state text,
    country text,
    is_active text,
    created_at text,
    updated_at text
);

CREATE TABLE goods_receipts (
    id INTEGER,
    purchase_order_id INTEGER,
    received_by_employee_id INTEGER,
    received_at text,
    notes text,
    created_at text
);

CREATE TABLE order_items (
    id INTEGER,
    order_id INTEGER,
    product_variant_id INTEGER,
    quantity INTEGER,
    unit_price text,
    icms_rate text,
    ipi_rate text,
    line_total text
);

CREATE TABLE brands (
    id INTEGER,
    name text,
    country text,
    is_active text,
    created_at text,
    updated_at text
);

CREATE TABLE fiscal_invoices (
    id INTEGER,
    order_id INTEGER,
    nfe_number text,
    nfe_access_key INTEGER,
    series INTEGER,
    issued_at text,
    status text,
    total_amount text,
    xml_storage_uri text,
    created_at text,
    updated_at text
);

CREATE TABLE employees (
    id INTEGER,
    full_name text,
    cpf INTEGER,
    email text,
    role text,
    primary_location_id INTEGER,
    hire_date text,
    termination_date text,
    is_active text,
    created_at text,
    updated_at text
);

CREATE TABLE purchase_order_items (
    id INTEGER,
    purchase_order_id INTEGER,
    product_variant_id INTEGER,
    quantity_ordered INTEGER,
    unit_cost text,
    line_total text
);

CREATE TABLE customers (
    id INTEGER,
    person_type text,
    legal_name text,
    trade_name text,
    tax_id INTEGER,
    state_registration text,
    email text,
    phone text,
    is_active text,
    created_at text,
    updated_at text
);

CREATE TABLE products (
    id INTEGER,
    name text,
    description text,
    brand_id INTEGER,
    category_id INTEGER,
    ncm_code INTEGER,
    unit_of_measure text,
    is_active text,
    created_at text,
    updated_at text
);

CREATE TABLE product_variants (
    id INTEGER,
    product_id INTEGER,
    sku text,
    barcode_ean INTEGER,
    sale_price text,
    cost_price text,
    weight_kg text,
    icms_rate text,
    ipi_rate text,
    is_active text,
    created_at text,
    updated_at text
);

CREATE TABLE return_items (
    id INTEGER,
    return_id INTEGER,
    order_item_id INTEGER,
    quantity text,
    action text,
    exchange_variant_id INTEGER,
    unit_refund_amount text
);

CREATE TABLE product_suppliers (
    product_variant_id INTEGER,
    supplier_id INTEGER,
    supplier_sku text,
    last_quoted_cost text,
    lead_time_days INTEGER,
    is_preferred text,
    created_at text,
    updated_at text
);

CREATE TABLE orders (
    id INTEGER,
    order_number text,
    channel text,
    customer_id INTEGER,
    salesperson_id INTEGER,
    location_id INTEGER,
    status text,
    subtotal text,
    discount_amount text,
    total text,
    placed_at text,
    created_at text,
    updated_at text
);

CREATE TABLE categories (
    id INTEGER,
    name text,
    slug text,
    parent_category_id INTEGER,
    is_active text,
    created_at text,
    updated_at text
);

CREATE TABLE stock_levels (
    product_variant_id INTEGER,
    location_id INTEGER,
    quantity_on_hand text,
    reorder_point INTEGER,
    updated_at text
);

CREATE TABLE variant_attribute_values (
    product_variant_id INTEGER,
    attribute_id INTEGER,
    value text
);

CREATE TABLE returns (
    id INTEGER,
    return_number text,
    order_id INTEGER,
    customer_id INTEGER,
    received_at_location_id INTEGER,
    status text,
    reason text,
    total_refund_amount text,
    created_at text,
    updated_at text
);

CREATE TABLE payments (
    id INTEGER,
    order_id INTEGER,
    method text,
    installments INTEGER,
    amount text,
    status text,
    paid_at text,
    created_at text,
    updated_at text
);
