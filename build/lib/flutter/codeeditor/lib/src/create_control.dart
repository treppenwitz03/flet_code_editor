import 'package:flet/flet.dart';

import 'codeeditor.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "codeeditor":
      return CodeeditorControl(
        parent: args.parent,
        control: args.control,
      );
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}
