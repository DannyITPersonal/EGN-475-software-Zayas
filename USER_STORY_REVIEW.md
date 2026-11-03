# User Story Review

Reviewed against INVEST. This document lists issues only; it does not rewrite the stories.

- **Story 2 — Place an Order:** Potentially too large: it spans selecting items, setting quantities, and submitting an order. Quantity constraints and what happens if an item becomes unavailable before submission are unspecified.
- **Story 3 — Receive Order Confirmation:** The required scope of “unique” is unclear (for example, whether order numbers must be unique across all orders or only active orders).
- **Story 5 — View Incoming Orders:** “Incoming” is ambiguous. The criteria do not establish which order statuses belong on the kitchen board.
- **Story 6 — Update Order Status:** The allowed status transitions are unclear. The criteria cover starting preparation and rejecting one rollback, but not the rest of the status lifecycle.
- **Story 7 — Manage Menu Items:** Combines adding and updating items, but the success criterion only covers adding. “Authorized” and “valid price” are undefined, leaving scope and expected behavior unclear.
- **Story 8 — Modify or Cancel an Order:** Too large: modification and cancellation are separate behaviors. “Modify” does not specify what can change, and the criteria do not define how cancellation works or precisely when preparation begins.

Stories 1 and 4 have no major size or testability issue. Story 4’s “current status” could be clearer about freshness. The acceptance criteria are generally testable as written; no story was assessed as wholly untestable.
