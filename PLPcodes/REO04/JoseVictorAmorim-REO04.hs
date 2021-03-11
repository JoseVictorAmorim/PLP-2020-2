statistics :: String -> (String, Int)
statistics word = (([head(word), '.', last(word)]), length(word))
  