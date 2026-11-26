##############
 Secure Shell
##############

Getting started with SSH/Secure Shell at Loyola.

The department provides two systems for general use:

-  **dijkstra.cs.luc.edu**: the :doc:`Dijkstra Computational Cluster
   </dijkstra/overview>`. This is the system you connect to with SSH,
   using your CS account.

-  **jhub.cs.luc.edu**: a JupyterHub server. It is a separate service
   from Dijkstra. When you are off campus, it is available only through
   the web. We add all students who take COMP 141. Other students can
   e-mail helpdesk@cs.luc.edu to request access.

***************************
 Connecting from off campus
***************************

SSH to Dijkstra is blocked outside of Loyola. When you are off campus,
you must first connect to the university VPN, and then connect to
Dijkstra as usual. There is no alternate SSH port. See :doc:`Virtual
Private Network </its_services/vpn>` for how to enroll.

***********
 Connecting
***********

SSH clients are built into macOS, Linux, and current versions of
Windows (use PowerShell or Windows Terminal). Open a terminal and run:

.. code:: bash

   ssh your-username@dijkstra.cs.luc.edu

Your CS account username matches your university login ID. If you do not
have an account, or need your password reset, see :doc:`User Accounts
</department_services/user_accounts>`.

Windows users who prefer a Linux environment can install the Windows
Subsystem for Linux (WSL) and use the same command from there.

*****************************
 Using SSH keys (recommended)
*****************************

SSH keys let you log in without typing your password each time, and are
more secure than passwords alone. You create a key pair: a private key
that stays on your computer, and a public key that you place on
Dijkstra.

#. Generate a key pair on your computer:

   .. code:: bash

      ssh-keygen -t ed25519

   Press Enter to accept the default location, and choose a passphrase.
   The passphrase protects your private key if someone gets a copy of
   it. It is never sent to Dijkstra. Never share your private key (the
   file without the ``.pub`` extension).

#. Copy the public key to Dijkstra. On macOS and Linux:

   .. code:: bash

      ssh-copy-id your-username@dijkstra.cs.luc.edu

   On Windows, where ``ssh-copy-id`` is not available, display your
   public key in PowerShell and copy the whole line:

   .. code:: powershell

      type $env:USERPROFILE\.ssh\id_ed25519.pub

   Then log in to Dijkstra with your password and add it (paste your
   key in place of the text in quotes):

   .. code:: bash

      mkdir -p ~/.ssh
      echo "PASTE-YOUR-PUBLIC-KEY-HERE" >> ~/.ssh/authorized_keys

#. Check the permissions on Dijkstra, which SSH requires to accept your
   key:

   .. code:: bash

      chmod 700 ~/.ssh
      chmod 600 ~/.ssh/authorized_keys

#. Connect again. You should be asked for your key passphrase (or
   nothing, if you chose none) instead of your account password:

   .. code:: bash

      ssh your-username@dijkstra.cs.luc.edu

Shortcut for repeated use
=========================

Add an entry to ``~/.ssh/config`` on your computer so that you can just
type ``ssh dijkstra``:

.. code:: text

   Host dijkstra
       HostName dijkstra.cs.luc.edu
       User your-username
       IdentityFile ~/.ssh/id_ed25519

****************
 Troubleshooting
****************

Connection timed out
   If you are off campus, make sure the university VPN is connected.

Permission denied
   Check your username and password. If you have forgotten your
   password, see :doc:`User Accounts
   </department_services/user_accounts>`. If you are using a key, check
   the permissions in step 3 above.

Other problems
   See :doc:`Getting Help </how_to/getting_help>`.

To transfer files, see :doc:`Remote Access </how_to/remote_access>`.
