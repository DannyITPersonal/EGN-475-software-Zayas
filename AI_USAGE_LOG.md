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

## Flask Menu and Order Workflow Assignment — November 24, 2026

**Project:** Café Calle Ocho Ordering Application  
**AI tool:** AI assistant using Copilot SDK in VS Code

AI assistance was used to implement and test the menu-management and kitchen-order workflows in the Flask application.

| Activity | AI assistance provided | Verification |
|---|---|---|
| Menu item editing and validation | Added an edit route and reusable `validate_item` function for required names, safe price conversion and limits, database-backed categories, and duplicate names ignoring case and extra spaces. | Exercised valid and invalid create/edit submissions with a temporary SQLite database; confirmed error messages and entered values were preserved. |
| Menu item deletion | Added a POST-only delete route with parameterized SQL. Items referenced by orders are marked unavailable rather than removed, preserving order records. | Confirmed GET is rejected, missing items return 404, unreferenced items are deleted, and referenced items remain available to existing orders. |
| Order status workflow | Added `NEXT_STATUS` and a POST-only status route for `received` → `preparing` → `ready` → `picked up`. | Tested valid and invalid transitions, including rejection after `picked up`, and verified database status values. |
| Kitchen board | Connected the board to SQLite and added status badges and POST buttons for only the next allowed transition. | Verified the kitchen route renders and each order has the appropriate next-step control. |
| Flash messages | Added shared flash display to `base.html`, so messages appear on pages extending it and are consumed after display. | Confirmed a message appeared once and was absent on the next page load. |
| Menu administration | Added `/admin/menu` with an item table and add, edit, and delete actions. Moved management controls off the customer-facing menu and redirected completed management actions to the admin page. | Tested the admin page and CRUD redirects; confirmed `/admin/menu` returned HTTP 200. |

### Assignment questions

1. **Why redirect after a successful form?**
   Redirecting after a successful POST follows Post/Redirect/Get: Flask saves the submission, then sends the browser to a page loaded with GET. This helps prevent a refresh from repeating the POST. In Interactive 5A, the missing redirect allowed a refresh to repeat the previous form submission, potentially saving the same information again.

2. **Why must delete use POST?**
   Deletion changes database state, so it should not be triggered by a GET request intended for retrieving a page. A browser prefetch, crawler, or other automated service could follow a GET delete link unintentionally. The delete form submits by POST, and the route accepts only POST.

3. **Which additional validation rule was added?**
   Menu item names are checked for duplicates after normalizing capitalization and extra whitespace. This helps prevent staff from adding the same item under slightly different spellings or spacing.

4. **What AI-assisted code was changed, and why?**
   The customer-facing menu originally contained Add, Edit, and Delete controls. Those administrative actions were moved to a dedicated menu-admin page because they did not belong on the customer menu. The delete action uses a POST form rather than a normal link.
