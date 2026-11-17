# UpperMyo v1.0

UpperMyo is a six-channel upper-limb surface electromyography (sEMG) dataset containing 264 recordings from 24 participants, covering eight upper-limb actions. The recordings are stored in `six_channel_dataset/`.

## Data format

The stored CSV labels correspond to the following actions and manuscript abbreviations:

| CSV label | Action | Abbreviation |
|---|---|---|
| `zq` | Hand opening | HO |
| `zqq` | Elbow flexion | EF |
| `zsz` | Elbow extension | EE |
| `wsz` | Wrist extension | WE |
| `wns` | Wrist ulnar deviation | UD |
| `wwz` | Wrist radial deviation | RD |
| `wq` | Hand closing | HC |
| `wqq` | Wrist flexion | WF |
| `none` | Background | BG |

Channels `channel1`–`channel6`, in order, are biceps brachii (BB), triceps brachii (TB), extensor carpi radialis (ECR), extensor carpi ulnaris (ECU), flexor carpi radialis (FCR), and flexor carpi ulnaris (FCU). The sampling rate is 1,000 Hz; timestamps are in microseconds (μs), and channel amplitudes are in microvolts (μV).

- `all_data_output.csv` contains a complete 70-second recording, including action and background samples.
- `valid_data_output.csv` contains five four-second action segments. A standalone `!!!` row marks the start of each segment and is not a signal sample; read timestamps within each segment.
- The action signals in the paired full and valid CSVs are identical and must not be treated as independent recordings.

## License

The UpperMyo dataset is released under the [Creative Commons Attribution 4.0 International license (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). See [LICENSE](LICENSE) for the full terms.

When sharing the dataset or an adaptation, credit the UpperMyo authors, link to this repository and the license, and indicate any changes.

Copyright (c) 2026 The UpperMyo authors.
