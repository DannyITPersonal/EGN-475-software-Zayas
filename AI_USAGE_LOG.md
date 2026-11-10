# AI Usage Log

**Project:** Café Calle Ocho Ordering Application  
**Date:** November 3, 2026  
**AI tool:** AI assistant using Copilot SDK in VS Code

## Purpose of AI assistance

AI assistance was used to review the supplied user stories against INVEST and to create static HTML mockups for the café ordering application. Requirements and sample data were supplied by the project owner.

## Work completed

| Activity | AI assistance provided |
|---|---|
| User story review | Identified potential size, ambiguity, and testability concerns in the supplied stories. The review was recorded in `USER_STORY_REVIEW.md`. |
| Customer menu mockup | Created `mockup/menu.html` with the requested navigation, menu categories, sample items and prices, and a link to the order page. |
| Order mockup | Created `mockup/order.html` with a sample order table, quantities, prices, total, and links to continue shopping or view confirmation. |
| Confirmation mockup | Created `mockup/confirmation.html` with a sample order number, order details, total, received status, and navigation links. |
| Order history mockup | Created `mockup/history.html` with an order-number form, sample order and status, and an example not-found message. |
| Kitchen board mockup | Created `mockup/kitchen.html` with three sample orders and status controls. |
| Menu administration mockup | Created `mockup/menu-admin.html` with a sample item table, an add-item form, and edit/save/cancel controls. |

## Requirements followed

- Used semantic HTML and the requested Pico CSS 2 stylesheet from jsDelivr.
- Used static sample data.
- Added no JavaScript, backend, or database functionality.
- Implemented the layouts from the written requirements; no separate wireframe files were provided in the reviewed materials.

## Verification performed

- Opened the menu, order, confirmation, history, kitchen, and menu administration pages in a browser and checked their rendered content.
- Followed the menu's **View Order** link to the order page.
- Followed the order page's **Place Order** link to the confirmation page.
- Followed the confirmation page's **Check Order Status** link to the history page.
- Ran `git diff --check` after the mockup changes.

## Limitations and review

The pages are visual prototypes. Add, remove, search, save, edit, cancel, and order-status controls do not update data or perform real operations. The order search and not-found message are illustrative only. Sample content and the resulting layouts should be reviewed and adjusted by the project owner before submission or implementation.

## Additional AI assistance — November 10, 2026

| Activity | AI assistance provided | Verification |
|---|---|---|
| Menu Jinja template | Updated `templates/menu.html` to extend `base.html`, display menu items grouped by category, format prices to two decimal places, and use `url_for()` for item and order links. | Requested `/menu` and checked item names, formatted prices, and generated links. |
| Kitchen Jinja template | Updated `templates/kitchen.html` to extend `base.html` and display each order in its own card, preserving the wireframe's order details and display-only status controls. | Requested `/kitchen` and checked all three sample orders and their customer, items, time, and status. Used bracket access for the `items` dictionary key to avoid Jinja resolving the dictionary method. |
| Menu detail route review | Reviewed the route's integer URL converter, in-memory item lookup by ID, and `abort(404)` behavior. No code change or database functionality was needed. | Confirmed an existing item returns 200, while an unknown ID and a non-integer path return 404. |
