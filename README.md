# checklist
Begin with the end in mind. Often a task or a project of mine ends with
a bunch of documents. For example, filing taxes require a set of
documents, preparing submissions and proposals do so too. I find it very effective to create a list which when checked off will mark the
completion of task or project for me.

checklist is a simple tool that lets me quickly list the documents that
are pending, delivered etc. by scanning the designated folder on my laptop or on shared storage.

It also helps in the team setting. Mashed-up with other tools it sends
quick status update and reminders to the team.

checklist --help --missing --status --all --delivered --unknown

--help
Displays this message.

--missing
Lists the missing documents from folder with an empty checkmark [ ].
This is the default behavior.

--status
Lists all documents from checklist.
Documents delivered have a checkmark in front.

--all
Lists all documents from checklist appended by unknown documents in
folder. Deliveries delivered have a checkmark in front [x]. Unknown
documents have a question mark [?].

--delivered
Lists delivered documents from checklist.

--unknown
Lists unknown documents in folder.

//TODO
Office folks like to use a concept of versioning. This is carried out by
appending a v0 or v1 at the end. I will not follow this approach here
as it will mix up the final documents with versioning which is best
done elsewhere.

//Sorting
Sort on Delivery Time
Sort on Delivery Status: Missing, Delivered, Unknown

//Not before --post
Sometimes documents need to be updated to be counted.
--post can be passed from command line or setup in the checklist

## Adding New Expected Files to the Checklist

You can add new expected files to the checklist from the command line using the `add_to_checklist.py` script. This script will add the specified file to the `checklist.txt` if it does not already exist.

### Usage

To add a new expected file to the checklist, run the following command:

```sh
python add_to_checklist.py <file_name>
```

Replace `<file_name>` with the name of the file you want to add to the checklist.

### Example

```sh
python add_to_checklist.py "ITR - FY2019-20 - 25a - New Document.pdf"
```

This command will add the file "ITR - FY2019-20 - 25a - New Document.pdf" to the `checklist.txt` if it does not already exist.

## Adding and Viewing Due Dates

You can now add optional due dates to each file in the checklist. The due dates should be in the format `YYYY-MM-DD`. If a file does not have a specific deadline, you can leave the due date blank.

### Example

Here is an example of how to add due dates to the files in `checklist.txt`:

```
ITR - FY2019-20 - 01a - Investment Proof Submission Form (12 BB).xls - 2023-12-01
ITR - FY2019-20 - 02a - H801 NOC from Spouse.DOC
ITR - FY2019-20 - 03a - H801 Home Loan Provisional Statement Bajaj.pdf - 2023-12-05
ITR - FY2019-20 - 04a - Capital Gains Raman Adlakha.csv
ITR - FY2019-20 - 05a - Capital Gains Raman Adlakha.pdf - 2023-12-10
ITR - FY2019-20 - 06a - Credit Card Payments Raman Adlakha.pdf
ITR - FY2019-20 - 07a - Investment Xactions Raman Adlakha.csv - 2023-12-15
ITR - FY2019-20 - 08a - Investment Xactions Raman Adlakha.pdf
ITR - FY2019-20 - 09a - Savings Interest Income Raman Adlakha.pdf - 2023-12-20
ITR - FY2019-20 - 10a - Form16.PDF
ITR - FY2019-20 - 11a - ASK Equity Capital Gains Tax Statement Raman Adlakha.pdf - 2023-12-25
ITR - FY2019-20 - 12a - ASK Realized Gain Losses statement Raman Adlakha.pdf
ITR - FY2019-20 - 13a - MF Investment Transaction Report Raman Adlakha.pdf - 2023-12-30
ITR - FY2019-20 - 14a - MF Realized Gain Loss Report Raman Adlakha.pdf
ITR - FY2019-20 - 15a - H801 Home Final Statement Bajaj.pdf - 2024-01-05
ITR - FY2019-20 - 16a - Insurance Premium Receipt Max Bupa 2 years.PDF
ITR - FY2019-20 - 17a - 26AS-Raman Adlakha.pdf - 2024-01-10
ITR - FY2019-20 - 18a - Declaration of Assets  Liability - Raman Adlakha.xlsx
ITR - FY2019-20 - 19a - Computation Raman Adlakha.pdf - 2024-01-15
ITR - FY2019-20 - 20a - Challan Raman Adlakha Direct Tax.pdf
ITR - FY2019-20 - 21a - Income Tax Return Raman Adlakha.pdf - 2024-01-20
ITR - FY2019-20 - 22a - Income Tax Return Verification Raman Adlakha.pdf
ITR - FY2019-20 - 23a - Invoice Raman Adlakha.pdf - 2024-01-25
ITR - FY2019-20 - 24a - Final Intimation from GoI Raman Adlakha adupaxxxxhddmmyyyy.pdf
```

### Viewing Due Dates

When you run the script, it will display the files along with their due dates (if any). This helps you keep track of deadlines and prioritize your tasks accordingly.
