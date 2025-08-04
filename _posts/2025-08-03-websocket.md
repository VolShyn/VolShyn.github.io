---
layout: post
title: "WebSocket"
category: programming
date: 2025-08-03
---

<sub> Protocol; A set of rules. <sub>

1. TOC
{:toc}

---

Used in WEB applications fot instant, continuous bidirectional (so-called **Full-Duplex** by time slots) data exchange between client and a server.

{% include info.html text="A server is a program or process that listens for incoming connections or requests, whilst a client is a program or process that initiates connections or sends requests"%}

{% include info.html text="Simplex - one-way communication (mobile network station). Half-Duplex - two-way, with one direction at a time (walkie-talkie)"%}

# The WEB part

It starts as HTTP and abides by web security rules.

A WS connection begins with a standard HTTP handshake. The client sends an HTTP request with a special **upgrade header**[^1] asking to switch to another protocol:

```http
GET /index.html HTTP/1.1
Host: ex.ua
Connection: Upgrade
Upgrade: ws/1, capybara/2
```

which means, that client wants a server to use another protocol, `ws` or `capybara`. The server can politely decline the proposed protocol change by sending a 200 OK response to the request, followed by the response body according to the usual rules of the HTTP protocol. Or the server may agree to switch protocols; in this case, it responds with `101 Switching Protocols`[^2], indicating in the response which of the protocols proposed by the client it has chosen:

```http
HTTP/1.1 101 Switching Protocols
Upgrade: ws/1
Connection: Upgrade
```

At this point, the persistent TCP connection remains open but is governed by the WS protocol. This handshake mechanism was designed so that WS can operate over the usual web ports (80/443) and traverse proxies, making them compatible with existing web infrastructure.

{% include info.html text="TCP ensures that bytes arrive in order and without errors (or not at all), handling retransmissions and packet ordering internally"%}

Once the upgrade is done, the client and server exchange messages in frames[^3] rather than independent HTTP requests, which is important, because WS messages incur very little overhead - after the initial HTTP upgrade, each message frame contains only a small header (as little as 2 bytes for small payloads). This contrasts with HTTP, where every request/response carries headers that can be larger than the data itself.

{% include info.html text="Before WS, web devs used hacks like polling (AJAX polling) or long-polling (a client repeatedly asking the server for updates)"%}

# The Socket part

**Socket** - is an abstract object, endpoint that allow sending and receiving data to/from another endpoint; Typically, a socket is defined by an IP address and port number at one end, paired with an IP and port at the other end (TCP/IP).

WS build on this concept: under the hood, a WS connection is implemented on top of a TCP socket connection. Sockets, overall, are more generic and are not restricted to the HTTP protocol. So we can implement any kind of communication with them. Just an example of how socket[^4] might look:

```
(TCP, local_IP, local_port, server_IP, server_port) 
(TCP, 8.8.8.4, 8080, 8.8.8.8, 8070) 
```

In the context of sockets, a server typically binds to a specific port on its host machine and waits for clients to connect to that port. Conceptually, a WS server is nothing more than an application listening on a TCP port that follows the WS protocol.

# Reading

[^1]: https://datatracker.ietf.org/doc/html/rfc2616#section-14.42
[^2]: https://datatracker.ietf.org/doc/html/rfc2616#section-10.1.2 
[^3]: https://datatracker.ietf.org/doc/html/rfc6455#section-5.1
[^4]: https://realpython.com/python-sockets/

