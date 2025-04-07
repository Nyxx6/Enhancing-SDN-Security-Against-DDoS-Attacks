# Research Notes on Flow Detection Methods in SDN Security

## Overview of Flow-Based Detection in SDN

Flow-based detection is fundamental to identifying and mitigating DDoS attacks in SDN environments. Understanding the characteristics of different flows and establishing appropriate detection criteria are essential for building an effective security system.

## Key Flow Characteristics in SDN

1. **Flow Definition in OpenFlow**:
   - A flow in OpenFlow is defined by a set of packet header fields
   - Typically includes source/destination IP addresses, source/destination ports, protocol
   - Can also include MAC addresses, VLAN tags, and other header information
   - Flow entries in switches contain match fields, counters, and actions

2. **Flow Types in SDN**:
   - **Control Flows**: Communication between controllers and switches
   - **Data Flows**: End-to-end communication between hosts
   - **Management Flows**: Network management and monitoring traffic

3. **Flow Granularity**:
   - **Fine-grained flows**: Specific matching on multiple header fields
   - **Coarse-grained flows**: Matching on fewer fields (e.g., only destination IP)
   - Trade-off between detection accuracy and resource consumption

## Flow Characteristics in DDoS Attack Scenarios

1. **Normal Flow Patterns**:
   - Relatively consistent packet rates
   - Bidirectional communication
   - Complete protocol handshakes
   - Predictable header field distributions
   - Moderate flow rule creation rate

2. **Attack Flow Patterns**:
   - **Volume-based attacks**: Extremely high packet rates
   - **Protocol-based attacks**: Incomplete handshakes, protocol violations
   - **Application-layer attacks**: Seemingly legitimate but resource-intensive requests
   - **Table-miss flooding**: High rate of new flows with randomized headers
   - **Control plane saturation**: High rate of packet-in messages to controller

3. **Data-to-Control Plane Saturation Attack Flows**:
   - High rate of unique flows with randomized header fields
   - Low probability of matching existing flow rules
   - Generate excessive packet-in messages to the controller
   - Often use spoofed source IP addresses
   - May target specific protocol fields to maximize processing overhead

## Flow Intensity Metrics

1. **Volume-Based Metrics**:
   - Packets per second (pps)
   - Bytes per second (bps)
   - Flows per second (fps)
   - Packet-in messages per second

2. **Distribution-Based Metrics**:
   - Entropy of source/destination IP addresses
   - Entropy of source/destination ports
   - Protocol distribution
   - Flow size distribution

3. **Temporal Metrics**:
   - Flow duration
   - Inter-arrival time between packets
   - Flow establishment rate
   - Flow rule timeout patterns

4. **Behavioral Metrics**:
   - Ratio of unidirectional to bidirectional flows
   - Completion rate of protocol handshakes
   - Symmetry of traffic volume in both directions
   - Response-to-request ratio

## Detection Methods in Existing Research

1. **Statistical Methods**:
   - **Threshold-based detection**: Setting fixed or adaptive thresholds for metrics
   - **Entropy-based detection**: Measuring randomness in header fields
   - **Correlation analysis**: Identifying relationships between different metrics
   - **Time series analysis**: Detecting anomalies in temporal patterns

2. **Machine Learning Methods**:
   - **Supervised learning**: Classification based on labeled training data
   - **Unsupervised learning**: Clustering and anomaly detection
   - **Deep learning**: Neural networks for complex pattern recognition
   - **Reinforcement learning**: Adaptive policy optimization

3. **Hybrid Methods**:
   - Combining statistical and machine learning approaches
   - Multi-stage detection pipelines
   - Ensemble methods for improved accuracy

## FlowKeeper's Approach to Flow Detection

1. **Traffic Agent Module (TAM)**:
   - Operates between data and control planes
   - Uses statistical thresholds for initial classification
   - Categorizes flows based on frequency:
     - Low frequency: Potential attacks, dropped immediately
     - High frequency: Legitimate traffic, forwarded to controller
     - Medium/ambiguous: Forwarded to GVAM for further analysis

2. **Global View Agent Module (GVAM)**:
   - Integrated within the controller
   - Uses SVM model for classification of suspicious traffic
   - Provides feedback to TAM for threshold adjustment
   - Maintains global view of network state

## Limitations in Current Approaches

1. **Fixed Thresholds**:
   - Lack adaptability to changing network conditions
   - May lead to high false positive/negative rates
   - Difficult to set appropriate values for diverse environments

2. **Centralized Detection**:
   - Creates single points of failure
   - Increases detection latency
   - May become overwhelmed during large-scale attacks

3. **Limited Context Awareness**:
   - Focus on individual metrics without considering relationships
   - Insufficient incorporation of network topology information
   - Lack of application-layer context

4. **Reactive Nature**:
   - Detection occurs after attack traffic reaches the control plane
   - Limited early warning capabilities
   - Potential for damage before mitigation begins

## Promising Research Directions

1. **Distributed Detection**:
   - Deploying detection agents at multiple points in the network
   - Collaborative detection through information sharing
   - Local decision-making with global coordination

2. **Multi-level Detection**:
   - Data plane level: Early detection at switches
   - Control plane level: Comprehensive analysis with global view
   - Host level: End-point monitoring and response

3. **Adaptive Thresholds**:
   - Dynamic adjustment based on network conditions
   - Machine learning for threshold optimization
   - Context-aware threshold selection

4. **Feature Engineering**:
   - Identification of most relevant flow characteristics
   - Creation of composite features for improved detection
   - Dimensionality reduction for efficient processing

5. **Behavioral Analysis**:
   - Profiling of normal network behavior
   - Detection of deviations from established patterns
   - Consideration of application-specific behavior
