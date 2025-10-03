# Personal Finance Tracker API - Test Cases

## 1. Authentication Test Cases

### 1.1 User Registration (`POST /auth/register`)

**Base Cases:**
1. Successfully register a new user with valid email, password, and required fields
2. Verify JWT tokens are returned upon successful registration
3. Verify default categories are created for new user
4. Verify user profile is returned with registration response

**Edge Cases:**
1. Register with minimum password length (8 characters)
2. Register with maximum allowed field lengths
3. Register with special characters in name fields
4. Register with various valid email formats (subdomain, plus addressing)
5. Register with different timezone formats
6. Register with all supported currency codes

**Null/Empty Cases:**
1. Attempt registration with missing email field
2. Attempt registration with missing password field
3. Attempt registration with missing first_name field
4. Attempt registration with missing last_name field
5. Attempt registration with null values for optional fields
6. Attempt registration with empty string values

**Validation Errors:**
1. Register with invalid email format
2. Register with password less than 8 characters
3. Register with password containing only numbers
4. Register with unsupported currency code
5. Register with invalid timezone
6. Register with email containing SQL injection attempts
7. Register with XSS attempts in name fields

**Conflict Cases:**
1. Register with an already existing email
2. Register with email differing only in case from existing user
3. Concurrent registration attempts with same email (race condition)

### 1.2 User Login (`POST /auth/login`)

**Base Cases:**
1. Successfully login with correct email and password
2. Verify access and refresh tokens are returned
3. Verify token expiry times are correct
4. Verify user profile is included in response

**Edge Cases:**
1. Login with email in different case than registered
2. Login immediately after registration
3. Login after password reset
4. Multiple simultaneous login attempts from same user
5. Login with email containing special characters

**Null/Empty Cases:**
1. Login with missing email field
2. Login with missing password field
3. Login with empty string email
4. Login with empty string password
5. Login with null values

**Authentication Failures:**
1. Login with incorrect password
2. Login with non-existent email
3. Login with deactivated account
4. Login with locked account (after multiple failures)
5. Login with expired account

**Rate Limiting:**
1. Multiple failed login attempts trigger rate limiting
2. Verify rate limit reset after time window
3. Successful login resets failure count

### 1.3 Token Refresh (`POST /auth/refresh`)

**Base Cases:**
1. Successfully refresh access token with valid refresh token
2. Verify new access token has correct expiry
3. Verify refresh token remains valid

**Edge Cases:**
1. Refresh token just before expiry
2. Refresh token immediately after generation
3. Multiple refresh requests in quick succession
4. Refresh during an active session

**Invalid Token Cases:**
1. Refresh with expired refresh token
2. Refresh with malformed token
3. Refresh with revoked token
4. Refresh with token from deleted user
5. Refresh with access token instead of refresh token
6. Refresh with empty token
7. Refresh with null token

**Race Conditions:**
1. Concurrent refresh requests with same token
2. Use old access token while refresh is in progress

## 2. Transaction Management Test Cases

### 2.1 List Transactions (`GET /transactions`)

**Base Cases:**
1. List all transactions for authenticated user
2. List transactions with default pagination (page 1, 20 items)
3. Verify transaction summaries (total income, expenses, net)
4. Verify transactions are sorted by date (newest first)

**Filtering Cases:**
1. Filter by transaction type (income only)
2. Filter by transaction type (expense only)
3. Filter by specific category
4. Filter by date range (date_from and date_to)
5. Filter by amount range (min_amount and max_amount)
6. Filter by payment method
7. Filter by tags (single tag)
8. Filter by tags (multiple tags)
9. Filter by recurring status
10. Search by description text
11. Combine multiple filters

**Pagination Cases:**
1. Request specific page number
2. Request custom page size
3. Request page beyond available data
4. Request with page_size = 1
5. Request with maximum page_size (100)
6. Request with page_size exceeding maximum

**Sorting Cases:**
1. Sort by date ascending
2. Sort by date descending
3. Sort by amount ascending
4. Sort by amount descending
5. Sort by category name

**Edge Cases:**
1. List transactions when user has none
2. List transactions with exactly one transaction
3. Filter with date_from after date_to
4. Filter with min_amount greater than max_amount
5. Search with special characters
6. Search with SQL injection attempts

**Authorization:**
1. List transactions without authentication token
2. List transactions with expired token
3. List transactions with invalid token
4. Verify user can only see their own transactions

### 2.2 Create Transaction (`POST /transactions`)

**Base Cases:**
1. Create income transaction with required fields only
2. Create expense transaction with all optional fields
3. Verify transaction appears in list after creation
4. Verify budget spending is updated after expense creation
5. Create transaction with tags

**Amount Cases:**
1. Create transaction with zero amount
2. Create transaction with decimal amount (2 decimal places)
3. Create transaction with decimal amount (more than 2 decimal places)
4. Create transaction with very large amount
5. Create transaction with negative amount (should fail)

**Date Cases:**
1. Create transaction with today's date
2. Create transaction with past date
3. Create transaction with future date
4. Create transaction with date in different timezone
5. Create transaction with invalid date format

**Category Cases:**
1. Create transaction with system category
2. Create transaction with user-defined category
3. Create transaction with non-existent category
4. Create transaction with deleted category
5. Create transaction with wrong type category (income category for expense)

**Edge Cases:**
1. Create transaction with very long description (at max length)
2. Create transaction with unicode characters in description
3. Create transaction with empty string description
4. Create multiple transactions rapidly (rate limiting)
5. Create transaction with duplicate tags in array

**Validation Errors:**
1. Create transaction missing type field
2. Create transaction missing amount field
3. Create transaction missing category_id field
4. Create transaction missing date field
5. Create transaction with invalid type value
6. Create transaction with invalid payment method

**Race Conditions:**
1. Create multiple transactions simultaneously
2. Create transaction while category is being deleted
3. Create transaction while budget is being updated

### 2.3 Update Transaction (`PUT /transactions/{id}`)

**Base Cases:**
1. Update transaction amount
2. Update transaction category
3. Update transaction description
4. Update transaction date
5. Update multiple fields at once

**Edge Cases:**
1. Update transaction to different type (income to expense)
2. Update only one field leaving others unchanged
3. Update with same values (no actual change)
4. Update transaction from recurring template
5. Update very old transaction

**Authorization:**
1. Update transaction belonging to another user
2. Update non-existent transaction
3. Update with expired token
4. Update deleted transaction

**Race Conditions:**
1. Concurrent updates to same transaction
2. Update transaction while it's being deleted
3. Update transaction while budget calculation is running

### 2.4 Delete Transaction (`DELETE /transactions/{id}`)

**Base Cases:**
1. Delete existing transaction
2. Verify transaction no longer appears in list
3. Verify budget spending is recalculated after deletion

**Edge Cases:**
1. Delete already deleted transaction (soft delete)
2. Delete transaction from recurring template
3. Delete oldest transaction
4. Delete newest transaction

**Authorization:**
1. Delete transaction belonging to another user
2. Delete non-existent transaction
3. Delete with invalid token

**Race Conditions:**
1. Delete transaction while it's being updated
2. Multiple concurrent deletion attempts

### 2.5 Bulk Transaction Creation (`POST /transactions/bulk`)

**Base Cases:**
1. Create 10 valid transactions in bulk
2. Create maximum allowed transactions (100) in bulk
3. Verify all transactions are created atomically

**Partial Failure Cases:**
1. Submit batch with some valid and some invalid transactions
2. Submit batch where middle transaction fails validation
3. Submit batch where last transaction fails
4. Verify rollback behavior on failure

**Edge Cases:**
1. Submit empty array of transactions
2. Submit single transaction via bulk endpoint
3. Submit more than maximum allowed (>100)
4. Submit duplicate transactions in same batch

**Performance:**
1. Measure time for maximum batch size
2. Verify no timeout for large batches

## 3. Category Management Test Cases

### 3.1 List Categories (`GET /categories`)

**Base Cases:**
1. List all categories (system + user)
2. List only expense categories
3. List only income categories
4. List only user-defined categories

**Hierarchy Cases:**
1. Verify parent-child relationships are preserved
2. List categories with multiple nesting levels
3. Verify orphaned subcategories handled correctly

**Edge Cases:**
1. List categories when user has no custom categories
2. List categories with circular parent references
3. List with invalid type filter

### 3.2 Create Category (`POST /categories`)

**Base Cases:**
1. Create income category with required fields
2. Create expense category with all fields
3. Create subcategory with parent_id
4. Create category with spending limit

**Validation Cases:**
1. Create category with duplicate name
2. Create category with empty name
3. Create category with very long name
4. Create category with invalid color format
5. Create category with invalid icon
6. Create category with non-existent parent_id
7. Create category with negative spending limit

**Edge Cases:**
1. Create category with parent from different type
2. Create deeply nested category (multiple levels)
3. Create category with unicode emoji as icon

### 3.3 Delete Category (`DELETE /categories/{id}`)

**Base Cases:**
1. Delete category without transactions
2. Delete category and reassign transactions
3. Delete parent category with children

**Edge Cases:**
1. Delete system category (should fail)
2. Delete category with active budget
3. Delete category referenced in recurring template
4. Delete already deleted category

**Race Conditions:**
1. Delete category while transaction is being created
2. Delete category while being updated

## 4. Budget Management Test Cases

### 4.1 Create Budget (`POST /budgets`)

**Base Cases:**
1. Create monthly budget for specific category
2. Create overall budget (no category specified)
3. Create budget with custom alert threshold
4. Create budget with rollover enabled

**Date/Period Cases:**
1. Create budget for current month
2. Create budget for future month
3. Create budget for past month
4. Create budget for December (year boundary)
5. Create budget for February (different day counts)

**Validation Cases:**
1. Create duplicate budget for same period/category
2. Create budget with zero amount
3. Create budget with negative amount
4. Create budget with invalid month (0 or 13)
5. Create budget with alert_percentage > 100

**Edge Cases:**
1. Create budget for category with existing transactions
2. Create budget for empty category
3. Create multiple budgets for different categories same month

### 4.2 Get Budget Progress (`GET /budgets/{id}`)

**Base Cases:**
1. Get budget with no spending
2. Get budget with partial spending (under limit)
3. Get budget at exactly 100% spent
4. Get budget over limit

**Edge Cases:**
1. Get budget for future period
2. Get budget for category with no transactions
3. Get budget during month transition
4. Get budget with rolled over amount from previous month

**Calculation Cases:**
1. Verify spending calculation includes all relevant transactions
2. Verify pending transactions handled correctly
3. Verify deleted transactions excluded from calculation
4. Verify recurring transactions included

### 4.3 Budget Alerts (`GET /budgets/alerts`)

**Base Cases:**
1. Get all alerts for user
2. Get only unread alerts
3. Mark alert as read
4. Verify alert generated at 80% threshold
5. Verify alert generated at 100% threshold

**Edge Cases:**
1. Get alerts when none exist
2. Get alerts for deleted budget
3. Multiple alerts for same budget
4. Alerts during budget update

## 5. Financial Goals Test Cases

### 5.1 Create Goal (`POST /goals`)

**Base Cases:**
1. Create emergency fund goal
2. Create vacation goal with all fields
3. Create debt payoff goal
4. Create goal with initial amount

**Calculation Cases:**
1. Verify monthly contribution calculation
2. Verify days remaining calculation
3. Verify on-track status calculation

**Validation Cases:**
1. Create goal with target date in past
2. Create goal with current amount > target amount
3. Create goal with zero target amount
4. Create goal with negative amounts

### 5.2 Add Contribution (`POST /goals/{id}/contributions`)

**Base Cases:**
1. Add contribution to active goal
2. Add contribution that completes goal
3. Add contribution with notes
4. Add backdated contribution

**Edge Cases:**
1. Add contribution exceeding target amount
2. Add negative contribution (withdrawal)
3. Add contribution to completed goal
4. Add contribution to paused goal

**Race Conditions:**
1. Multiple simultaneous contributions
2. Add contribution while goal being deleted

## 6. Analytics Test Cases

### 6.1 Financial Summary (`GET /analytics/summary`)

**Base Cases:**
1. Get daily summary
2. Get weekly summary
3. Get monthly summary
4. Get yearly summary

**Edge Cases:**
1. Get summary for period with no transactions
2. Get summary for partial period (mid-month)
3. Get summary for future period
4. Get summary spanning year boundary

**Calculation Verification:**
1. Verify income total is correct
2. Verify expense total is correct
3. Verify net calculation
4. Verify savings rate calculation
5. Verify top categories are accurate
6. Verify comparison percentages

### 6.2 Cash Flow Analysis (`GET /analytics/cashflow`)

**Base Cases:**
1. Get historical cash flow only
2. Get cash flow with forecast
3. Verify running balance calculation
4. Verify forecast based on recurring transactions

**Edge Cases:**
1. Cash flow for user with no transactions
2. Cash flow with negative balance periods
3. Cash flow for single day
4. Cash flow for multiple years

## 7. Data Management Test Cases

### 7.1 Export Data (`POST /data/export`)

**Base Cases:**
1. Export all data in JSON format
2. Export all data in CSV format
3. Export specific date range
4. Export specific data types only

**Edge Cases:**
1. Export with no transactions
2. Export very large dataset (>10000 transactions)
3. Export with special characters in data
4. Export with null values in optional fields

**Security:**
1. Verify export URL expires after time limit
2. Verify export URL cannot be accessed by other users
3. Verify sensitive data properly included/excluded

### 7.2 Import Data (`POST /data/import`)

**Base Cases:**
1. Import valid CSV with all required columns
2. Import with column mapping
3. Import with automatic category matching
4. Verify duplicate detection works

**Error Handling:**
1. Import with missing required columns
2. Import with invalid data types
3. Import with malformed CSV
4. Import file too large
5. Import with invalid date formats
6. Import with invalid amounts

**Edge Cases:**
1. Import empty CSV
2. Import single row CSV
3. Import with BOM characters
4. Import with different line endings (CRLF vs LF)
5. Import with quoted fields containing commas
6. Import with different encodings (UTF-8, ISO-8859-1)

**Performance:**
1. Import 1000 transactions
2. Import 5000 transactions
3. Verify timeout handling for large files

## 8. Concurrency and Race Condition Tests

### 8.1 Transaction Race Conditions
1. Create transaction while updating budget for same category
2. Delete category while creating transaction for it
3. Multiple clients updating same transaction simultaneously
4. Create recurring transaction while processing scheduled transactions

### 8.2 Budget Race Conditions
1. Update budget while alerts are being generated
2. Multiple expense transactions hitting budget limit simultaneously
3. Delete budget while transaction is being created
4. Rollover budget calculation during month transition

### 8.3 Goal Race Conditions
1. Multiple contributions to same goal simultaneously
2. Update goal while contribution being added
3. Complete goal from multiple contribution sources

### 8.4 Data Consistency
1. Verify account balance consistency during concurrent transactions
2. Verify budget spending accuracy with parallel transactions
3. Verify category spending limits with concurrent expenses
4. Verify goal progress with simultaneous contributions

## 9. Performance and Load Tests

### 9.1 Response Time Requirements
1. List transactions: < 500ms for 100 items
2. Create transaction: < 200ms
3. Analytics summary: < 1s for monthly data
4. Export data: < 5s for 1000 transactions

### 9.2 Concurrent User Load
1. 100 concurrent users creating transactions
2. 500 concurrent users viewing analytics
3. 50 concurrent imports processing
4. 1000 concurrent API requests across endpoints

### 9.3 Data Volume Tests
1. User with 10,000 transactions
2. User with 1,000 categories
3. User with 5 years of historical data
4. Database with 1 million total transactions

## 10. Security Tests

### 10.1 Authentication/Authorization
1. Verify JWT tokens expire correctly
2. Verify refresh tokens can be revoked
3. Verify user can only access own data
4. Test privilege escalation attempts
5. Verify API key scoping (when implemented)

### 10.2 Input Validation
1. SQL injection attempts in all text fields
2. XSS attempts in user-generated content
3. Command injection in file imports
4. Path traversal in file operations
5. JSON injection in API requests

### 10.3 Rate Limiting
1. Verify rate limits per user
2. Verify rate limit headers in response
3. Verify rate limit reset
4. Test distributed rate limiting across multiple servers

### 10.4 Data Privacy
1. Verify password hashing (never stored plain text)
2. Verify sensitive data encryption at rest
3. Verify PII data in logs is redacted
4. Verify data export includes only user's own data
5. Test account deletion removes all user data