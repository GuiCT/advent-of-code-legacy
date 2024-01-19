import Debug.Trace (trace)

lookAndSay :: String -> String
lookAndSay "" = ""
-- lookAndSay "3" -> "13" (One Three)
lookAndSay [c] = '1' : [c]
-- lookAndSay "13" -> "1113" (One One, One Three)
lookAndSay str = currentDigit ++ rest
  where
    -- Compare everything in string to head, count how many then append
    currentDigit = show (length $ takeWhile (== h) str) ++ [h]
    -- Recursively deal with rest, skip current digits
    rest = lookAndSay $ dropWhile (== h) str
    -- Define head and tail
    (h : t) = str

main :: IO ()
main = do
  -- Compose lookAndSay, applying it 40 times
  -- Get the length and print it
  print "Part one"
  print (length $ foldr ($) "3113322113" (replicate 40 lookAndSay))
  print "Part two"
  print (length $ foldr ($) "3113322113" (replicate 50 lookAndSay))
