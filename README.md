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
