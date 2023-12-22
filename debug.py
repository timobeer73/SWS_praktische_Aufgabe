import functions as f


args = None

publicKey, cipherText, relationsAmount = f.readFile(args)
plainTextArray = f.generatePlainText(args, relationsAmount)
cipherTextsArray = f.calculateCipherText(args, publicKey, plainTextArray)
matrix = f.calculateMatrix(args, plainTextArray, cipherTextsArray)
