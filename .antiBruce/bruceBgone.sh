echo 'bruce will not be annoying while this program is activated'

w
echo ' '
read $sessions

for word in $sessions
do
    if [$word=='pi']; then
        echo 'pi user'
fi
done
