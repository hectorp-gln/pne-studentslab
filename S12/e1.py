# http://127.0.0.1:8080/hello
    # Which is the request line?
    # => GET /hello HTTP/1.1
    # Which is the resource that the client is asking for? (the path)
    # => "hello"

# http://127.0.0.1:8080/file.html
    # Which is the request line?
    # => GET /file.html HTTP/1.1
    # Which is the resource that the client is asking for? (the path)
    # => "file.html"

# http://127.0.0.1:8080/hi/there?name=virus&type=corona
    # Which is the request line?
    # => GET /hi/there?name=virus&type=corona HTTP/1.1
    # Which is the resource that the client is asking for? (the path)
    # => "hi/there?name=virus&type=corona"