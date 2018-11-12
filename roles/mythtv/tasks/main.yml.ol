---
- name: Install kodi
  apt: name=kodi state=latest
  with_items:
    - kodi
    - mplayer
    - vlc
    - libva2
    - libva-x11-2
    - vdpauinfo
    - vdpau-va-driver
    - minidlna
    - ubuntu-restricted-addons
    - ubuntu-restricted-extras
    - xine-ui
    - totem 
      #    - mediatomb
- name: Firewall config
  # not support due to this module using python2
  # firewalld: service={{item}} permanent=yes immediate=yes state=enabled
  shell: "firewall-cmd --add-service={{item}} --permanent"
  with_items:
    - 'http'
    - 'https'
- name: Firewall ports allow
  shell: "firewall-cmd --add-port={{item}} --permanent"
  with_items:
    - '8080/tcp'
    - '8080/udp'
    - '8200/tcp'
    - '8200/udp'
      #notify: 
      #- restart firewalld
    #handlers:
- name: restart firewalld
  service: name=firewalld state=reloaded
