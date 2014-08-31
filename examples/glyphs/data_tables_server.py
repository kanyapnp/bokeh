from __future__ import print_function

from bokeh.browserlib import view
from bokeh.document import Document
from bokeh.objects import ColumnDataSource
from bokeh.sampledata.autompg import autompg
from bokeh.session import Session
from bokeh.widgets import TableColumn, HandsonTable, PivotTable, HBox

document = Document()
session = Session()
session.use_doc('data_tables_server')
session.load_document(document)

source = ColumnDataSource(autompg)

fields = zip(autompg.columns, map(str, autompg.dtypes))
columns = [
    TableColumn(data=column, type="text" if dtype == "object" else "numeric", header=column)
    for column, dtype in fields
]

data_table = HandsonTable(source=source, columns=columns)
pivot_table = PivotTable(source=source, fields=[ dict(name=field, dtype=dtype) for field, dtype in fields ])

hbox = HBox(children=[data_table, pivot_table])

document.add(hbox)
session.store_document(document)

if __name__ == "__main__":
    link = session.object_link(document.context)
    print("Please visit %s to see the plots" % link)
    view(link)
    print("\npress ctrl-C to exit")
