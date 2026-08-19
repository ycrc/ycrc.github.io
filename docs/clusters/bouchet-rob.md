# Bouchet HPC Cluster — Rules of Behavior

By requesting and logging into a Bouchet account, you agree to abide by these rules, the [YCRC HPC Policies](https://research.computing.yale.edu/computing-resources/hpc-policies), and Yale's [IT Appropriate Use Policy (Policy 1607\)](https://your.yale.edu/policies-procedures/1607-information-technology-appropriate-use-policy). Bouchet is for research computing only; use for commercial purposes or in violation of Yale policy is prohibited. Violations may result in account suspension or revocation and referral for University disciplinary action.

---

## 1\. Before You Begin

**Complete Yale's required security awareness training.** You must complete Yale's ["Bee Cyber Fit at Yale" security awareness training](https://www.myworkday.com/yale/learning/program/7efc4b6091bb103ac148232b72aa0000?record=e2db0804d64e1023bfb7497b97bc0001&type=2d29754fdb8e100008b50ff6bc94003b) before your account is created, and keep it current.

---

## 2\. Your Account

**Your account may not be shared.** Your account is issued to you individually. Never share your password, SSH private key, or any other login credential with anyone. You are responsible for all activity that occurs under your account.

**Protect your SSH key with a strong passphrase.** If you authenticate via SSH key, your private key must be protected by a passphrase that meets [Yale's password requirements](https://cybersecurity.yale.edu/use-secure-passwords). Do not copy your private key to other systems.

**Keep your contact information current.** Your account must be associated with a valid email address at all times; accounts with invalid addresses will be locked. If your email is changing (for example, if you are transitioning off a Yale address), notify YCRC before it stops working.

**Notify YCRC when your affiliation changes.** If you are leaving your research group or Yale, notify YCRC directly. Transfer ownership of shared files before departing.

---

## 3\. Your Computer

**Your local machine must lock automatically.** Any device used to connect to Bouchet — including personal laptops — must lock and require a password after no more than **45 minutes of inactivity**.

---

## 4\. Using the Cluster

**Do not run computation on login or transfer nodes.** Login nodes are for connecting, managing files, and submitting jobs. Transfer nodes are for moving data only. All computation must be submitted through the Slurm job scheduler.

**Use partitions as intended and release idle resources.** Submit jobs only to partitions suited to your workload and within their stated limits. End interactive and Open OnDemand sessions when you are done — idle sessions will be canceled without warning.

**Avoid patterns that stress shared resources.** Do not submit large numbers of very short jobs (under five minutes) or run workflows that generate thousands of small files, as these degrade performance for all users. Contact YCRC before running such workflows at scale.

**Do not circumvent resource policies.** Bouchet's compute nodes and GPUs are shared resources that depend on all users acting in good faith. Deliberately designing jobs to circumvent fair-use policies is prohibited. Accounts found doing so will be locked immediately and without advance notice.

---

## 5\. Your Data

**Confirm your data is approved for Bouchet before storing it.** Bouchet supports research data including approved sensitive data. If you are unsure whether your data is appropriate, ask YCRC first.

**DUA-governed data requires prior YCRC approval.** If your data is covered by a Data Use Agreement, provide a copy to YCRC and receive explicit approval before storing any covered data. Your PI is responsible for informing YCRC which users are authorized to access covered data.

**You are the steward of your data.** You are responsible for ensuring your data is handled in compliance with all applicable agreements and Yale policies, including any retention, disposition, or access restrictions. Set file permissions so sensitive files are not accessible to other users. Delete data when it is no longer required by your research or data agreements.

**Do not use scratch for long-term storage.** Scratch is purged automatically after 60 days; artificially extending file lifetimes is prohibited. Contact YCRC if you need additional persistent storage.

**Backups are limited.** Only home and project directories are backed up, for approximately 30 days. No other storage is backed up. Maintain your own copies of critical data elsewhere.

---

## 6\. Security and Incidents

**Report suspected security incidents immediately.** If your account may be compromised, you notice unusual activity, or you have accidentally exposed sensitive data, contact:

- **YCRC:** [research.computing@yale.edu](mailto:research.computing@yale.edu)  
- **Yale ISO:** [Report an Incident](https://cybersecurity.yale.edu/get-help/report/report-incident)

When in doubt, report. Do not attempt to access systems or data you are not authorized to use, bypass security controls, or assist others in doing so. Authentication and system activity on Bouchet are logged and may be reviewed for security and compliance purposes.  