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

## Week 4 — SQLite database schema — November 17, 2026

**Project option:** Option A — Cuban café ordering system

AI assistance was used to create `schema.sql` for the Café Calle Ocho Flask project based on the project owner's requested tables and constraints.

| Activity | AI assistance provided | Verification |
|---|---|---|
| Database schema | Created `users`, `menu_items`, `orders`, and `order_items` tables. Added auto-incrementing integer primary keys, foreign-key references, SQLite-compatible defaults, integer prices in cents, boolean-style availability values, the `received` order-status default, and a default quantity of 1. Added drop statements in dependency order so the schema can rebuild the database. | Executed the script twice with SQLite; verified the sample data, requested defaults, and foreign-key integrity. |
| Sample data | Added six realistic Café Calle Ocho menu items and three guest sample orders, with order-item rows linking each order to menu items. | Confirmed the seeded menu, orders, and order items were present after execution. |

## Week 4 — Assignment 2: User-Testing Feedback — November 17, 2026

**Project:** Café Calle Ocho Ordering Application
**Project option:** Option A — Cuban café ordering system

AI assistance was used to organize the supplied user-testing results and prepare submission-ready feedback decisions and GitHub issue descriptions.

| Activity | AI assistance provided | Verification |
|---|---|---|
| Feedback organization | Organized the results from two testers for price lookup, category browsing, menu-item submission, and kitchen-board use. | Checked the decisions against the observed tester feedback and only applied fixes for reported confusion. |
| Priority decisions | Separated requested changes into fix next week, fix later, and not a problem. | Confirmed that the sandwich price was reported as easy to find by both testers and that category and save-confirmation concerns were reported by multiple testers. |
| GitHub issue preparation | Prepared issue titles and descriptions for category visibility and post-save confirmation. | Confirmed that the issue text requests the `feedback` label but no issue links were fabricated; the project owner must create them in the own GitHub repository. |

### Feedback decisions

| Feedback or issue | Decision | Reason |
|---|---|---|
| Menu category headings are not easy to notice. | Fix next week | Both testers needed extra time to locate or confirm the Drinks section. Clearer category separation should improve browsing. |
| The result of saving a new menu item is not obvious. | Fix next week | A clear success message or redirect would reassure staff that the item was saved. |
| Add photos or more detailed descriptions to menu items. | Fix later | This could improve the menu, but the basic browsing and menu-management tasks are more important for the next version. |
| The Cuban sandwich price was easy to find. | Not a problem | Both testers found the price without help, so no change is needed based on this test. |

### Prepared GitHub issues

**Issue 1 title:** Make menu categories easier to identify

**Issue 1 description:** During user testing, the Drinks category was not immediately noticeable. Improve the visual separation of menu categories so customers can scan the menu more easily. Add the feedback label.

**Issue 1 URL:** Not created yet

**Issue 2 title:** Show a clear confirmation after adding a menu item

**Issue 2 description:** After staff submit the menu item form, show a clear success message or redirect that confirms the item was saved. This should make the result of the action easier to understand. Add the feedback label.

**Issue 2 URL:** Not created yet
