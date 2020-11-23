# Kernel

[Home](https://github.com/gabekiriakos/Nebulae) | [Installation](../documentation/installation.md) | [Kernel](../documentation/kernel.md) | [Management](../documentation/management.md)

<b>Hardware:</b>
* CPU: [AMD Ryzen 3600 @ 4.2Ghz](https://www.amd.com/en/products/cpu/amd-ryzen-5-3600)
* RAM: [G.Skill FlareX 3200Mhz 16GB](https://www.gskill.com/product/165/170/1535961634/F4-3200C14D-16GFX-Overview)
* Disk: [WD SN550 NVMe SSD](https://www.westerndigital.com/products/internal-drives/wd-blue-nvme-ssd)
* GPU: [Gigabyte NVIDIA GTX 1660 SUPER](https://www.gigabyte.com/Graphics-Card/GV-N166SOC-6GD#kf)
* Mobo: [ASUS ROG STRIX B450-I GAMING](https://rog.asus.com/Motherboards/ROG-Strix/ROG-STRIX-B450-I-GAMING-Model/)
* Modules: 
    * [Intel Corporation I211 Gigabit Network Connection](https://ark.intel.com/content/www/us/en/ark/products/64404/intel-ethernet-controller-i211-at.html)
    * [Realtek RTL8822BE WiFi/Bluetooth](https://www.realtek.com/en/products/communications-network-ics/item/rtl8822be)
* Peripherals: 
    * [Razer BlackWidow Lite](https://www.razer.com/gaming-keyboards/Razer-BlackWidow-Lite/RZ03-02640200-R3U1)
    * [Logitech G403 Hero](https://www.logitechg.com/en-us/products/gaming-mice/g403-hero-gaming-mouse.html)

<br>

The following configurations are personal so it is wise to read up on [configuring the kernel](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel). <br>
To make things easier, `emerge --ask sys-apps/pciutils` and run `lspci` to get hardware information for your specific build. <br>
Keep in mind that for network adapters to work correctly, they must be installed as <ins>modules</ins>. <br>
Included in this repo is the [kernel config](/usr/src/linux/.config) with most of these settings and more that can be loaded during `make menuconfig`.

<br>

```bash
KERNEL Enabling NTFS over FUSE using NTFS-3G
File systems  --->
    <*> FUSE (Filesystem in Userspace) support

KERNEL (Skype)
General setup  --->
    -*- Namespaces support  ---> 
        [*]   User namespace

KERNEL Enabling devtmpfs support
Device Drivers --->
  Generic Driver Options --->
    [*] Maintain a devtmpfs filesystem to mount at /dev
    [*]   Automount devtmpfs at /dev, after the kernel mounted the rootfs

KERNEL Enabling SCSI disk support
Device Drivers --->
   SCSI device support  --->
      <*> SCSI disk support

KERNEL Selecting necessary file systems
File systems --->
  <*> Second extended fs support
  <*> The Extended 3 (ext3) filesystem
  <*> The Extended 4 (ext4) filesystem
  <*> Reiserfs support
  <*> JFS filesystem support
  <*> XFS filesystem support
  <*> Btrfs filesystem support
  DOS/FAT/NT Filesystems  --->
    <*> MSDOS fs support
    <*> VFAT (Windows-95) fs support
 
Pseudo Filesystems --->
    [*] /proc file system support
    [*] Tmpfs virtual memory file system support (former shm fs)

KERNEL Activating SMP support
Processor type and features  --->
  [*] Symmetric multi-processing support

KERNEL Activating USB support for input devices
Device Drivers --->
  HID support  --->
    -*- HID bus support
    <*>   Generic HID driver
    [*]   Battery level reporting for HID devices
      USB HID support  --->
        <*> USB HID transport layer
  [*] USB support  --->
    <*>     xHCI HCD (USB 3.0) support
    <*>     EHCI HCD (USB 2.0) support
    <*>     OHCI HCD (USB 1.1) support

KERNEL Selecting processor types and features
Processor type and features  --->
   [ ] Machine Check / overheating reporting 
   [ ]   Intel MCE Features
   [ ]   AMD MCE Features
   Processor family (AMD-Opteron/Athlon64)  --->
      ( ) Opteron/Athlon64/Hammer/K8
      ( ) Intel P4 / older Netburst based Xeon
      ( ) Core 2/newer Xeon
      ( ) Intel Atom
      ( ) Generic-x86-64
      
Binary Emulations  --->
   [*] IA32 Emulation

KERNEL Enable support for GPT
-*- Enable the block layer --->
   Partition Types --->
      [*] Advanced partition selection
      [*] EFI GUID Partition support

KERNEL Enable support for UEFI
Processor type and features  --->
    [*] EFI runtime service support 
    [*]   EFI stub support
    [*]     EFI mixed-mode support
 
Firmware Drivers  --->
    EFI (Extensible Firmware Interface) Support  --->
        <*> EFI Variable Support via sysfs

KERNEL Kernel 4.11.0
Processor type and features  --->
  [*] Symmetric multi-processing support
  [*] AMD ACPI2Platform devices support
  Processor family (Opteron/Athlon64/Hammer/K8)  --->
    (X) Opteron/Athlon64/Hammer/K8
  [*] Supported processor vendors  --->
    [*]   Support AMD processors (NEW)
  [*] SMT (Hyperthreading) scheduler support
  [*] Multi-core scheduler support
  [*] Machine Check / overheating reporting
  [*]   AMD MCE features
  Performance monitoring  --->
    <*> AMD Processor Power Reporting Mechanism
  [*]   AMD microcode loading support
Power management and ACPI options  --->
  CPU Frequency scaling  --->
      Default CPUFreq governor (ondemand)  --->
    <*>   ACPI Processor P-States driver
    <*>   AMD Opteron/Athlon64 PowerNow!
    <*>   AMD frequency sensitivity feedback powersave bias
Device Drivers  --->
  Generic Driver Options --->
    (amd-ucode/microcode_amd_fam17h.bin) External firmware blobs to build into the kernel binary
    (/lib/firmware) Firmware blobs root directory
  [*] IOMMU Hardware Support  --->
    [*]   AMD IOMMU support
    <*>     AMD IOMMU Version 2 driver
  [*] Hardware Monitoring support --->
    [*]   AMD Family 10h+ temperature sensor

FILE /etc/portage/make.confZen2 compiler optimization
CFLAGS="-O2 -march=znver2"

KERNEL Enable loadable module support
[*] Enable loadable module support --->
Processor type and features --->
   [*] MTRR (Memory Type Range Register) support
Device Drivers --->
   Graphics support --->
      [*] VGA Arbitration
Device Drivers --->
   Character devices --->
      [*] IPMI top-level message handler

KERNEL Disable support for the in-kernel driver
Device Drivers --->
    Graphics support --->
        Frame buffer Devices --->
            <*> Support for frame buffer devices --->
              [*]   Simple framebuffer support
            < >   nVidia Framebuffer Support
            < >   nVidia Riva support
Device Drivers  --->
    Graphics support  --->
        < > Nouveau (nVidia) cards
        
root #lspci | grep --color Ethernet

KERNEL
Device Drivers  --->
    Networking support  --->
        [*] Network device support --->
            [*]   Ethernet driver support  --->

Scan the drivers carefully. Compare the results of the lspci command above with the available drivers in the list. Enable the feature(s) that match the installed Ethernet device(s). 

KERNEL linux-4.19

[*] Networking support  --->
    [*] Wireless  --->
        <M>   cfg80211 - wireless configuration API
        [ ]     nl80211 testmode command
        [ ]     enable developer warnings
        [ ]     cfg80211 certification onus
        [*]     enable powersave by default
        [ ]     cfg80211 DebugFS entries
        [ ]     support CRDA
        [ ]     cfg80211 wireless extensions compatibility
        <M>   Generic IEEE 802.11 Networking Stack (mac80211)
        [*]   Minstrel
        [*]     Minstrel 802.11n support
        [ ]       Minstrel 802.11ac support
              Default rate control algorithm (Minstrel)  --->
        [ ]   Enable mac80211 mesh networking (pre-802.11s) support
        -*-   Enable LED triggers
        [ ]   Export mac80211 internals in DebugFS
        [ ]   Trace all mac80211 debug messages
        [ ]   Select mac80211 debugging features  ----

[*] Networking support  --->
    [*] Wireless  --->
        [*]     cfg80211 wireless extensions compatibility

Device Drivers  --->
    [*] Network device support  --->
        [*] Wireless LAN  --->
 
            Select the driver for your Wifi network device, e.g.:
            <M> Broadcom 43xx wireless support (mac80211 stack) (b43)
            [M]    Support for 802.11n (N-PHY) devices
            [M]    Support for low-power (LP-PHY) devices
            [M]    Support for HT-PHY (high throughput) devices
            <M> Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
            <M>    Intel Wireless WiFi DVM Firmware support                             
            <M>    Intel Wireless WiFi MVM Firmware support
            <M> Intel Wireless WiFi 4965AGN (iwl4965)
            <M> Intel PRO/Wireless 3945ABG/BG Network Connection (iwl3945)
            <M> Ralink driver support  --->
                <M>   Ralink rt27xx/rt28xx/rt30xx (USB) support (rt2800usb)
 
-*- Cryptographic API --->
    -*- AES cipher algorithms
    -*- AES cipher algorithms (x86_64)
    <*> AES cipher algorithms (AES-NI)

Device Drivers  --->
    [*] LED Support  --->
        <*>   LED Class Support
 
[*] Networking support  --->
    [*] Wireless  --->
        [*] Enable LED triggers

root #emerge --ask sys-kernel/linux-firmware

KERNEL Enabling Bluetooth support
[*] Networking support --->
      <M>   Bluetooth subsystem support --->
              [*]   Bluetooth Classic (BR/EDR) features
              <*>     RFCOMM protocol support
              [ ]       RFCOMM TTY support
              < >     BNEP protocol support
              [ ]       Multicast filter support
              [ ]       Protocol filter support
              <*>     HIDP protocol support
              [*]     Bluetooth High Speed (HS) features
              [*]   Bluetooth Low Energy (LE) features
                    Bluetooth device drivers --->
                      <M> HCI USB driver
                      <M> HCI UART driver
      <*>   RF switch subsystem support --->
    Device Drivers --->
          HID support --->
            <*>   User-space I/O driver support for HID subsystem
            
KERNEL Linux 4.4.x
Device Drivers  --->
  <*> NVM Express block device

```
