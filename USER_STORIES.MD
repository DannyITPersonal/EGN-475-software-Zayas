
# Café Calle Ocho — User Stories and Acceptance Criteria

**Project:** Café Calle Ocho Ordering System
**Option:** A — Cuban Café Ordering Application
**Course:** EGN 475

## Story 1 — View the Digital Menu
**Priority:** Must

As a customer, I want to view the café's menu and prices, so that I can decide what food and drinks I want to order.

**Acceptance Criteria**

1. Given the café has available menu items, when a customer opens the menu, then the application displays item names, descriptions, and prices.
2. Given a menu item is marked as sold out, when a customer views the menu, then the item is marked unavailable and cannot be selected.

## Story 2 — Place an Order
**Priority:** Must

As a customer, I want to select menu items and quantities, so that I can submit an order for pickup.

**Acceptance Criteria**

1. Given a customer has selected available menu items and quantities, when they submit their order, then the application creates an order containing the selected items.
2. Given a customer has not selected any items, when they try to submit an order, then the application displays an error asking them to select at least one item.

## Story 3 — Receive Order Confirmation
**Priority:** Must

As a customer, I want to receive an order confirmation with an order number, so that I can identify my order when picking it up.

**Acceptance Criteria**

1. Given a customer successfully submits an order, when the application processes it, then a confirmation page displays a unique order number and order details.
2. Given an order submission fails, when the customer attempts to place the order, then the application displays an error instead of showing a false confirmation.

## Story 4 — Check Order Status
**Priority:** Must

As a customer, I want to check my order's current status, so that I know whether my food is being prepared or is ready for pickup.

**Acceptance Criteria**

1. Given a customer has a valid order number, when they check their order, then the application displays its current status.
2. Given a customer enters an order number that does not exist, when they search for the order, then the application displays an order not found message.

## Story 5 — View Incoming Orders
**Priority:** Must

As a kitchen staff member, I want to view incoming customer orders on one screen, so that I can organize the orders that need to be prepared.

**Acceptance Criteria**

1. Given customers have submitted orders, when kitchen staff open the kitchen board, then the application displays order numbers, items, and statuses.
2. Given there are no incoming orders, when kitchen staff open the kitchen board, then the application displays a message indicating that there are currently no orders.

## Story 6 — Update Order Status
**Priority:** Must

As a kitchen staff member, I want to update an order's status, so that customers and employees can see its preparation progress.

**Acceptance Criteria**

1. Given an order has been received, when kitchen staff select Start Preparing, then the order status changes to preparing.
2. Given an order has already been marked as picked up, when staff attempt to change it back to preparing, then the application prevents the invalid status change and displays an error.

## Story 7 — Manage Menu Items
**Priority:** Should

As an authorized café staff member, I want to add or update menu items, so that customers can see accurate menu information.

**Acceptance Criteria**

1. Given an authorized staff member enters a valid item name and price, when they save the item, then the application adds it to the menu.
2. Given a staff member attempts to save an item without a name or valid price, when they submit the form, then the application displays an error and does not save the invalid item.

## Story 8 — Modify or Cancel an Order
**Priority:** Should

As a customer, I want to modify or cancel my order before preparation begins, so that I can correct mistakes or change my mind.

**Acceptance Criteria**

1. Given an order has been received but preparation has not started, when the customer requests a modification or cancellation, then the application allows the change and updates the order accordingly.
2. Given kitchen staff have already started preparing the order, when the customer attempts to modify or cancel it, then the application prevents the change and displays an explanation.
