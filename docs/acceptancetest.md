### Acceptance Test Cases

This application should enable the admin to partially create accounts for freelancers and freelancers should be able to upload spreadsheets containing the task and generate the invoice. This invoice should then be downloaded.

### Flow

- Admin partially create freelancer and hand over the username and password to the freelancer
- Freelancer signs in and first thing to do are;
  - update password if need be
  - fill in information for the;
    - profile
    - address
    - company
    - assignment
- Freelancer can upload spreadsheet containing tasks in a specific format, then
  - provide a few information about the invoice
  - generate invoice
  - view invoice if need be
  - delete invoice if need be
  - download invoice
- Freelancer invoice is deleted after downloaded or it will be auto-deleted after 24 hours if the freelancer had not downloaded.

#### Admin - Create freelancer's IAM account

- Given that a user is not registered
- And I register the user
  - Register users using the IAM idea. Either using custom or auto-generated passwords and the option for a user to update the password
- The list of users should include the newly registered user with with his/her password, username and other information

#### Admin - Reset freelancer's password

- Given that a freelancer has forgotten the password
- And I reset the password
- The list of freelancer should contain the freelancer with the password updated.
- And the freelancer should be able to login with the newly updated password

#### Admin - Deactivate/Activate and Delete

- Given that a freelancer is suspended, or not working anymore the company
- And I deactivate their account, they shouldn't be able to perform normal operations like uploading spreadsheet, generating invoice, etc.
- And I delete their account, they shouldn't be able to log in to the application.

#### Admin - See the list of all registered freelancers

- Given that I am signed in as an Admin
- When I request to see the list of all freelancers
- This list appears with few details about each freelancer
- I can then expand to see more and more detail per freelancer

#### Freelancer - Generate invoice in PDF

- Given that I have uploaded a spreadsheet containing tasks in the required format
- And I request for a download
- The pdf file should be downloaded and stored in my local machine.

#### Freelancer - Upload a spreadsheet

- Given that I am signed in as a freelancer
- And I upload a spreadsheet containing tasks in the required format
- I should be able to generate an invoice from that spreadsheet

#### Freelancer - Configure my profile

- Given that I am signed in as a freelancer
- And I configure my profile
- Any generated invoice should auto-fill with information from my profile.

#### Freelancer - update/change my password

- Given that I am signed in as a freelancer
- And I update my password
- Next time I sign in, it should be with the new password to get me in.
